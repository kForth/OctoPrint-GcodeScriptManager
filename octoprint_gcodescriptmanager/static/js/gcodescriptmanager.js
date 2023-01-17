/*
 * View model for OctoPrint-GcodeScriptManager
 *
 * Author: Kestin Goforth
 * License: AGPLv3
 */
$(function () {
    function GcodeScriptManagerViewModel(parameters) {
        var self = this;

        self.settingsView = parameters[0];

        self.consts = {};
        self.scripts = ko.observableArray([]);

        self.editDialog = $("#dialog_gcodescriptmanager_editscript");
        self.editTarget = ko.observable(undefined);
        self.tempScript = ko.observable(undefined);

        self.onBeforeBinding = function () {
            self._settings = self.settingsView.settings.plugins.gcodescriptmanager;
            self.consts = ko.mapping.toJS(self._settings.consts);
            self._updateSettings(self._settings, self);
        };

        self.onSettingsBeforeSave = function () {
            self._updateSettings(self, self._settings);
        };

        self._updateSettings = function (source, target) {
            target.scripts(source.scripts());
        };

        self.addScript = function () {
            self.scripts.push(
                ko.mapping.fromJS({
                    name: self.getNewScriptName(),
                    type: "afterPrintDone",
                    when: "afterDefaultScript",
                    script: "",
                    enabled: false,
                    sidebarToggle: false
                })
            );
        };

        self.removeScript = function (script) {
            let index = self.scripts().indexOf(script);
            self.scripts.splice(index, 1);
        };

        self.duplicateScript = function (script) {
            let duplicate = $.extend({}, script);
            self.scripts.push(duplicate);
            self.editScript(duplicate);
        };

        self.editScript = function (script) {
            self.editTarget(script.index);
            self.tempScript(script);
            self.editDialog.modal("show");
        };

        self.nameInvalid = function () {
            return !!tempScript.name();
        };

        self.isEditFormValid = function (script) {
            return true;
        };

        self.saveEditScript = function (script) {
            self.scripts.splice(self.editTarget.index, 1, self.editTarget.script);
        };

        self.canMoveUp = function (script) {
            let index = self.scripts().indexOf(script);
            return index > 0;
        };

        self.canMoveDown = function (script) {
            let index = self.scripts().indexOf(script);
            return index < self.scripts().length - 1;
        };

        self.moveScriptUp = function (script) {
            self._moveScript(script, -1);
        };

        self.moveScriptDown = function (script) {
            self._moveScript(script, 1);
        };

        self._moveScript = function (script, distance) {
            let index = self.scripts().indexOf(script);
            if (self.canMoveDown(script)) {
                self.removeScript(script);
                self.scripts.splice(index + distance, 0, script);
            }
        };

        self.getNewScriptName = function () {
            let names = _.map(self.scripts(), function (s) {
                return s.name();
            });
            let name = gettext("New Script");
            let i = 0;
            while (_.includes(names, name)) {
                name = gettext("New Script") + " " + ++i;
            }
            return name;
        };

        self.getPopoverTitle = function (script) {
            return "<b>" + script.name() + "</b>";
        };

        self.getPopoverContent = function (script) {
            return [
                "<b>" + gettext("Type") + ":</b> " + _.startCase(script.type()),
                "<b>" + gettext("When") + ":</b> " + _.startCase(script.when()),
                "<b>" + gettext("Script") + ":</b><pre>" + script.script() + "</pre>"
            ].join("<br>");
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: GcodeScriptManagerViewModel,
        dependencies: ["settingsViewModel"],
        elements: [
            "#settings_plugin_gcodescriptmanager",
            "#sidebar_plugin_gcodescriptmanager",
            "#tab_plugin_gcodescriptmanager"
        ]
    });
});
