/*  Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
    License MIT (https://opensource.org/licenses/MIT). */
odoo.define("database_expiration.main", function(require) {
    "use strict";

    var AppsMenu = require("web.AppsMenu");

    AppsMenu.include({
        start: function() {
            this._super.apply(this, arguments);

            if (odoo.session_info.database_expiration_message) {
                this.$el
                    .find(".expiration_message")
                    .show()
                    .html(odoo.session_info.database_expiration_message);
            }

            if (odoo.session_info.is_database_expired) {
                $(".o_action_manager").block({
                    message: $(".block_ui_expiration_message"),
                });
                $("header").css("z-index", $.blockUI.defaults.baseZ + 20);
            }
        },
    });
});
