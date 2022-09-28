import octoprint.plugin

from .const import TYPE, TYPE_OPTIONS, WHEN, WHEN_OPTIONS


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
                "typeOptions": TYPE_OPTIONS,
                "whenOptions": WHEN_OPTIONS
            },
            "scripts": [
                {
                    "name": "Power Off After Print",
                    "type": TYPE.AFTER_PRINT_DONE,
                    "when": WHEN.AFTER_DEFAULT,
                    "script": "M81",
                    "enabled": False,
                    "sidebarToggle": True,
                }
            ],
        }

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        self.read_settings()

    def read_settings(self):
        self._scripts = self._settings.get(["scripts"])

    def write_settings(self):
        self._settings.set(["scripts"], self._scripts)
        self._settings.save()

    ##~~ AssetPlugin mixin

    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
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
                "name": "GcodeScriptManager Plugin",
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

        prefix, suffix = "", ""
        for script in self._scripts:
            if script["type"] == script_name:
                self._logger.info(
                    "Adding Gcode Script '%(name)s' on '%(type)s', '%(when)s'", script
                )
                if script["when"] == WHEN.BEFORE_DEFAULT:
                    prefix += "\n" + script["script"]
                else:
                    suffix += "\n" + script["script"]

        return prefix, suffix, {}

    ##~~ Softwareupdate hook

    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "gcodescriptmanager": {
                "displayName": "GcodeScriptManager Plugin",
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


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "GcodeScriptManager Plugin"


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = GcodeScriptManagerPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
        "octoprint.comm.protocol.scripts": __plugin_implementation__.gcode_script_hook,
    }
