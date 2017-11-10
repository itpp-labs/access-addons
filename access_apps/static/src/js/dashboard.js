odoo.define('access_apps.dashboard', function (require) {
"use strict";

    var dashboard = require('web_settings_dashboard');

    dashboard.Dashboard.include({

        start: function(){
            if(!odoo.session_info.has_access_to_apps) {
                this.$('.o_web_settings_dashboard_apps').parent().remove();
                this.all_dashboards = _.without(this.all_dashboards, 'apps');
	    }
            return this._super();
        }

   });
});
