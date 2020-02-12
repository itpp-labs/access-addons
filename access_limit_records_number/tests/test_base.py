# -*- coding: utf-8 -*-
from odoo.tests import common


@common.at_install(False)
@common.post_install(True)
class TestBase(common.TransactionCase):
    def test_users(self):
        demo_user = self.env.ref("base.user_demo")

        # ok
        self.env["base.limit.records_number.test"].sudo(demo_user).create(
            {"name": "r1"}
        )

        # limit 1 is reached
        with self.assertRaises(Exception):
            self.env["base.limit.records_number.test"].sudo(demo_user).create(
                {"name": "r2"}
            )
