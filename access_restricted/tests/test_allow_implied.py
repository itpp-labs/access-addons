# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase


class TestAllowImplied(TransactionCase):
    at_install = True
    post_install = True

    def test_base(self):
        demo_user = self.env.ref('base.user_demo')

        group_user = self.env.ref('base.group_user')
        group_system = self.env.ref('base.group_system')

        demo_user.write({'groups_id': [(3, group_user.id)]})
        demo_user.write({'groups_id': [(4, group_system.id)]})

        self.env['res.groups'].sudo(demo_user.id)._update_user_groups_view()

        TestConfigSettings = self.env['test.config.settings']
        test_config_settings = TestConfigSettings.create({'group_user': True})
        print '\n\n\n', 'TestConfigSettings', TestConfigSettings, 'test_config_settings', test_config_settings, '\n\n\n'
        test_config_settings.execute()
