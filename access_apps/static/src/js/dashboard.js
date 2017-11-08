odoo.define('access_apps.dashboard', function (require) {
"use strict";

    var dashboard = require('web_settings_dashboard');

    dashboard.Dashboard.include({

        init: function(parent, data){
            var ret = this._super(parent, data);
	    this.has_access_to_apps = data.has_access_to_apps;
            if(!this.has_access_to_apps) {
                this.all_dashboards = _.without(this.all_dashboards, 'apps');
	    }
            return ret;
        },

        start: function(){
            if(!this.has_access_to_apps) {
                this.$('.o_web_settings_dashboard_apps').parent().remove();
	    }
            return this._super();
        }

   });
});
