odoo.define('access_apps.dashboard', function (require) {
"use strict";

    var dashboard = require('web_settings_dashboard');
    var Model = require('web.Model');

    dashboard.Dashboard.include({

        willStart:function(){
            var self = this;
	    var Users = new Model('res.users');
		return Users.call('has_group', ['access_apps.group_allow_apps']).then(function (result) {
			self.has_access_to_apps = result;
		});
        },

        start: function(){
            if(!this.has_access_to_apps) {
		this.all_dashboards = _.without(this.all_dashboards, 'apps');
                this.$('.o_web_settings_dashboard_apps').parent().remove();
	    }
            return this._super();
        },

        load_apps: function(data){
            if(this.has_access_to_apps) {
                return this._super(data);
            }
            this.$('.o_web_settings_dashboard_apps').parent().remove();
        }
   });
});
