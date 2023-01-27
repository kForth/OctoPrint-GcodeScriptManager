import octoprint.plugin
from jinja2 import BaseLoader, Environment

from .const import (
    DEFAULT_SCRIPTS,
    ON_CONNECT,
    ON_CONNECT_OPTIONS,
    TYPE,
    TYPE_OPTIONS,
    WHEN,
    WHEN_OPTIONS,
)


class GcodeScriptManagerPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.StartupPlugin,
):
    def __init__(self):
        super().__init__()

        defaults = self.get_settings_defaults()
        self._scripts = defaults["scripts"]
        self._update_settings()

    def _update_client_settings(self):
        self._plugin_manager.send_plugin_message(
            self._identifier,
            {
                "settings": {
                    "scripts": self._scripts,
                }
            },
        )

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            "consts": {
                "onConnectOptions": ON_CONNECT_OPTIONS,
                "typeOptions": TYPE_OPTIONS,
                "whenOptions": WHEN_OPTIONS
            },
            "scripts": DEFAULT_SCRIPTS,
        }

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.read_settings()

    def read_settings(self):
        self._scripts = self._settings.get(["scripts"])
        self._update_settings()

    def _update_settings(self):
        self._enabled_script_types = set(sum(
            [[ss["type"] for ss in s["scripts"]] for s in self._scripts],
            start=[]
        ))

    def write_settings(self, notify=True):
        self._settings.set(["scripts"], self._scripts)
        self._settings.save()
        if notify:
            self._update_client_settings()

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/gcodescriptmanager.js"],
            "css": ["css/gcodescriptmanager.css"],
            "less": ["less/gcodescriptmanager.less"],
        }

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        return [
            {
                "type": "settings",
                "name": "GCODE Script Manager",
                "template": "gcodescriptmanager_settings.jinja2",
                "custom_bindings": True,
            },
            {
                "type": "sidebar",
                "name": "GCODE Scripts",
                "template": "gcodescriptmanager_sidebar.jinja2",
                "custom_bindings": True,
                "icon": "fas fa-scroll",
            },
        ]

    ##~~ StartupPlugin mixin

    def on_after_startup(self):
        self.read_settings()
        return super().on_after_startup()

    ##~~ GcodeScript Hook

    def gcode_script_hook(self, comm, script_type, script_name, *args, **kwargs):
        if not script_type == "gcode":
            return None
        if script_name not in self._enabled_script_types:
            return None

        should_save = False
        prefix, suffix = "", ""
        context = {
            "printer_profile": comm._printerProfileManager.get_current_or_default(),
            "last_position": comm.last_position,
            "last_temperature": comm.last_temperature.as_script_dict(),
            "last_fanspeed": comm.last_fanspeed,
        }

        if script_name in (TYPE.AFTER_PRINT_PAUSED, TYPE.BEFORE_PRINT_RESUMED):
            context.update(
                {
                    "pause_position": comm.pause_position,
                    "pause_temperature": comm.pause_temperature.as_script_dict(),
                    "pause_fanspeed": comm.pause_fanspeed,
                }
            )
        elif script_name == TYPE.AFTER_PRINT_CANCELLED:
            context.update(
                {
                    "cancel_position": comm.cancel_position,
                    "cancel_temperature": comm.cancel_temperature.as_script_dict(),
                    "cancel_fanspeed": comm.cancel_fanspeed,
                }
            )

        loader = BaseLoader()
        for script in self._scripts:
            if not script["enabled"]:
                continue
            for _script in script["scripts"]:
                if _script["type"] == script_name:
                    self._logger.info(
                        "Adding Gcode Script '%(name)s' on '%(type)s', '%(when)s'",
                        {
                            "name": script["name"],
                            "type": _script["type"],
                            "when": _script["when"],
                        }
                    )
                    template = Environment(loader=loader).from_string(_script["script"])
                    rendered = template.render(**context)

                    if _script["when"] == WHEN.BEFORE_DEFAULT:
                        prefix += "\n" + rendered
                    else:
                        suffix += "\n" + rendered

                    if script["autoDisable"]:
                        script["enabled"] = False
                        should_save = True

        if should_save:
            self.write_settings()

        return prefix, suffix, {}

    ##~~ HandleConnect Hook

    def handle_connect_hook(self, *args, **kwargs):
        if any([e['onConnect'] != ON_CONNECT.UNCHANGED for e in self._scripts]):
            for script in self._scripts:
                if script["onConnect"] == ON_CONNECT.ENABLED:
                    self._logger.info(
                        "Enabling Script on Connect: '%(name)s'",
                        {"name": script["name"]}
                    )
                    script["enabled"] = True
                elif script["onConnect"] == ON_CONNECT.DISABLED:
                    self._logger.info(
                        "Disabling Script on Connect: '%(name)s'",
                        {"name": script["name"]}
                    )
                    script["enabled"] = False
            self.write_settings()

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "gcodescriptmanager": {
                "displayName": "GCODE Script Manager",
                "displayVersion": self._plugin_version,
                # version check: github repository
                "type": "github_release",
                "user": "kforth",
                "repo": "OctoPrint-GcodeScriptManager",
                "current": self._plugin_version,
                # update method: pip
                "pip": "https://github.com/kforth/OctoPrint-GcodeScriptManager/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "GCODE Script Manager"

__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = GcodeScriptManagerPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
        "octoprint.comm.protocol.scripts": __plugin_implementation__.gcode_script_hook,
        "octoprint.printer.handle_connect": __plugin_implementation__.handle_connect_hook,
    }
