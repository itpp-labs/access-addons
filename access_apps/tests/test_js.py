# -*- coding: utf-8 -*-
import odoo.tests


@odoo.tests.common.at_install(False)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_dashboard_remove(self):
        demo_user = self.env.ref('base.user_demo')
        system_group = self.env.ref('base.group_system')
        allow_apps_group = self.env.ref('access_apps.group_allow_apps')
        demo_user.write({'groups_id': [(4, system_group.id)]})
        demo_user.write({'groups_id': [(3, allow_apps_group.id)]})
        self.phantom_js("/", "odoo.__DEBUG__.services['web_tour.tour'].run('removed_apps_dashboard')", "odoo.__DEBUG__.services['access_apps.dashboard'].ready.state() == 'resolved'", login="demo")
