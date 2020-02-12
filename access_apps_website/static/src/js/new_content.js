/*  Copyright 2018 Rafis Bikbov <https://www.it-projects.info/team/RafiZz>
    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html). */
odoo.define("access_apps_website.newMenu", function(require) {
    "use strict";
    var core = require("web.core");
    var Dialog = require("web.Dialog");

    var _t = core._t;

    var WebsiteNewMenu = require("website.newMenu");

    WebsiteNewMenu.include({
        /**
         * @override
         */
        _onModuleIdClick: function(ev) {
            var self = this;
            var _super = this._super;
            var selfArgs = arguments;

            var $el = $(ev.currentTarget);
            var $p = $el.find("a p");

            var title = $p.text();

            var moduleId = $el.data("module-id");
            var name = $el.data("module-shortdesc");

            ev.stopPropagation();
            ev.preventDefault();

            this._rpc({
                model: "ir.module.module",
                method: "search_read",
                domain: [["id", "=", moduleId]],
                fields: ["state"],
                limit: 1,
            }).then(function(data) {
                var moduleIsInstalled = data.length && data[0].state === "installed";
                if (moduleIsInstalled) {
                    return _super.apply(self, selfArgs);
                }

                self._rpc({
                    model: "res.users",
                    method: "has_group",
                    args: ["access_apps.group_allow_apps"],
                }).then(function(has_group) {
                    if (has_group) {
                        return _super.apply(self, selfArgs);
                    }

                    var msg = _t('"%s" App is not installed in the system.');
                    var content = _.str.sprintf(msg, name);
                    var buttons = [
                        {
                            text: _t("Cancel"),
                            close: true,
                        },
                    ];

                    new Dialog(this, {
                        title: title,
                        size: "medium",
                        $content: $("<p/>", {text: content}),
                        buttons: buttons,
                    }).open();
                });
            });
        },
    });
});
