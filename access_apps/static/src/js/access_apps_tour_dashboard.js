odoo.define('access_apps.tour', function (require) {
    'use strict';

    var tour = require("web_tour.tour");

    tour.register('removed_apps_dashboard', {
        test: true,
        url: '/web',
    },
        [
            {
                trigger: '.o_app[data-menu="4"], .oe_menu_toggler[data-menu="4"]',
                content: "Configuration options are available in the Settings app.",
                position: "bottom"
            },
            {
                content: "finish",
                trigger: '.o_web_settings_dashboard_invitations .o_web_settings_dashboard_header:not(:empty)',
                run: function(){
                    if ($('.o_web_settings_dashboard_apps')) {
                        console.log("error", "The apps dashboard is not removed");
                    } else {
                        console.log("Everything is ok");
                    }
                }
            }
        ]
    );

});
