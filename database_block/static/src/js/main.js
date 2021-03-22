/*  Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
    License MIT (https://opensource.org/licenses/MIT). */
odoo.define("database_block.main", function(require) {
    "use strict";

    var AppsMenu = require("web.AppsMenu");

    AppsMenu.include({
        start: function() {
            this._super.apply(this, arguments);

            if (odoo.session_info.database_block_message) {
                $(".database_block_message").html(
                    odoo.session_info.database_block_message
                );

                if (!odoo.session_info.database_block_is_warning) {
                    $(".o_action_manager").block({
                        message: $(".block_ui.database_block_message").html(
                            odoo.session_info.database_block_message
                        ),
                    });
                    $("header").css("z-index", $.blockUI.defaults.baseZ + 20);
                }

                if (odoo.session_info.database_block_show_message_in_apps_menu) {
                    $(".dropdown-menu > .database_block_message").show();
                }
            }
        },
    });
});
