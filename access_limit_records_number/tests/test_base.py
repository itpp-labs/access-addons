# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from openerp.tests import common


@common.tagged('post_install', '-at_install')
class TestBase(common.TransactionCase):

    def test_users(self):
        demo_user = self.env.ref('base.user_demo')

        # ok
        self.env['base.limit.records_number.test'].sudo(demo_user).create({'name': 'r1'})

        # limit 1 is reached
        with self.assertRaises(Exception):
            self.env['base.limit.records_number.test'].sudo(demo_user).create({'name': 'r2'})
