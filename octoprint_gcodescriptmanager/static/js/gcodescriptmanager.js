/*
 * View model for OctoPrint-GcodeScriptManager
 *
 * Author: Kestin Goforth
 * License: AGPLv3
 */
$(function () {
    function GcodeScriptManagerViewModel(parameters) {
        var self = this;

        // Injection Parameters
        self.settingsView = parameters[0];

        // HTML Elements
        self.editDialog = $("#dialog_gcodescriptmanager_editscript");
        self.confirmDeleteDialog = $("#dialog_gcodescriptmanager_confirmremove");

        // Constants
        self.typeOptions = [];
        self.whenOptions = [];
        self.typeMap = {};
        self.whenMap = {};

        // Observables
        self.scripts = ko.observableArray([]);
        self.editIndex = ko.observable(-1);
        self.tempScript = ko.mapping.fromJS({
            name: undefined,
            description: undefined,
            enabled: false,
            sidebarToggle: false,
            scripts: []
        });

        self._translateOptions = function (opts) {
            return _.map(opts, function (e) {
                return {value: e.value, label: gettext(e.label)};
            });
        };
        self._optionsToMap = function (opts) {
            return Object.fromEntries(
                _.map(opts, function (e) {
                    return [e.value, e.label];
                })
            );
        };

        self.onBeforeBinding = function () {
            let settings = self.settingsView.settings.plugins.gcodescriptmanager;
            self.scripts(settings.scripts());
            self.typeOptions = self._translateOptions(
                ko.mapping.toJS(settings.consts.typeOptions)
            );
            self.whenOptions = self._translateOptions(
                ko.mapping.toJS(settings.consts.whenOptions)
            );
            self.typeMap = self._optionsToMap(self.typeOptions);
            self.whenMap = self._optionsToMap(self.whenOptions);
        };

        self._getNewScriptName = function (base) {
            let i = 0;
            if (base) {
                let match = /^(.*)\s+\((\d+)\)$/.exec(base);
                if (match) {
                    base = match[1];
                    i = parseInt(match[2]);
                }
            } else {
                base = gettext("New Script");
            }
            const names = _.map(self.scripts(), function (s) {
                return s.name();
            });
            let name = base;
            while (_.includes(names, name)) {
                name = _.sprintf("%(base)s (%(i)d)", {base, i: ++i});
            }
            return name;
        };

        self.addScript = function () {
            let script = ko.mapping.fromJS({
                name: self._getNewScriptName(),
                description: gettext("A new script, not yet configured."),
                enabled: false,
                sidebarToggle: false,
                scripts: [
                    {
                        type: "afterPrintDone",
                        when: "afterDefaultScript",
                        script: ""
                    }
                ]
            });
            self.editScript(script);
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
            if (self.canMoveUp(script)) self._moveScript(script, -1);
        };

        self.moveScriptDown = function (script) {
            if (self.canMoveDown(script)) self._moveScript(script, 1);
        };

        self._moveScript = function (script, distance) {
            let index = self.scripts().indexOf(script);
            self.scripts.splice(index, 1);
            self.scripts.splice(index + distance, 0, script);
        };

        self.editScript = function (script) {
            self.editIndex(self.scripts().indexOf(script));
            _.forEach(_.pairs(ko.mapping.fromJS(script)), function ([k, v]) {
                console.log(
                    k,
                    self.tempScript[k],
                    typeof self.tempScript[k],
                    v,
                    typeof v
                );
                if (typeof v === "function") self.tempScript[k](v());
            });
            self.editDialog.modal("show");
        };

        self.editDialog_addSubscript = function () {
            self.tempScript.scripts.push({
                type: "afterPrintDone",
                when: "afterDefaultScript",
                script: ""
            });
        };

        self.editDialog_save = function () {
            if (self.editIndex() < 0) {
                self.scripts.push(ko.mapping.fromJS(ko.mapping.toJS(self.tempScript)));
            } else {
                _.forEach(_.pairs(ko.mapping.toJS(self.tempScript)), function ([k, v]) {
                    self.scripts()[self.editIndex()][k](v);
                });
            }
            self.editDialog.modal("hide");
        };

        self.editDialog_confirmRemove = function () {
            self.confirmDeleteDialog.modal("show");
        };

        self.editDialog_remove = function () {
            self.scripts.splice(self.editIndex(), 1);
            self.confirmDeleteDialog.modal("hide");
            self.editDialog.modal("hide");
        };

        self.editDialog_duplicate = function () {
            let script = ko.mapping.fromJS(ko.mapping.toJS(self.tempScript));
            script.name(self._getNewScriptName(script.name()));
            self.editScript(script);
        };

        self.editDialog_isEditMode = ko.pureComputed(function () {
            return self.editIndex() >= 0;
        });

        self.editDialog_isAddMode = ko.pureComputed(function () {
            return !self.editDialog_isEditMode();
        });

        self.editDialog_nameInvalid_empty = ko.pureComputed(function () {
            return !self.tempScript.name();
        });

        self.editDialog_nameInvalid_duplicate = ko.pureComputed(function () {
            const scriptName = self.tempScript.name();
            for (let i = 0; i < self.scripts().length; i++) {
                if (i == self.editIndex()) continue;
                if (self.scripts()[i].name() === scriptName) return true;
            }
            return false;
        });

        self.editDialog_nameInvalid = ko.pureComputed(function () {
            return (
                self.editDialog_nameInvalid_empty() ||
                self.editDialog_nameInvalid_duplicate()
            );
        });

        self.editDialog_formInvalid = ko.pureComputed(function () {
            return self.editDialog_nameInvalid();
        });

        self.getPopoverTitle = function (script) {
            return "<b>" + script.name() + "</b>";
        };

        self.getPopoverContent = function (script) {
            return script.description();
            // return _.map(script.scripts(), function (e) {
            //     return [
            //         "<b>" + gettext("Type") + ":</b> " + self.typeMap[e.type()],
            //         "<b>" + gettext("When") + ":</b> " + self.whenMap[e.when()],
            //         "<b>" + gettext("Script") + ":</b><pre>" + e.script() + "</pre>"
            //     ].join("<br>");
            // });
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
