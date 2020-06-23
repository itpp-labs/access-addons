# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import exceptions
from odoo.tests import common


@common.tagged("post_install", "-at_install")
class TestExcludedUsers(common.TransactionCase):
    def test_create(self):
        admin_user = self.env.ref("base.user_admin")
        Users = self.env["res.users"].with_user(admin_user)
        login = "test_excluded_user"
        rule_record = self.env.ref("access_limit_max_users.max_users_limit")
        rule_record.max_records = Users.search_count(
            [("is_excluded_from_limiting", "=", False)]
        )

        vals = {"name": login, "login": login, "is_excluded_from_limiting": True}

        with self.assertRaises(exceptions.ValidationError):
            Users.create(vals)

        Users.sudo().create(vals)

    def test_write(self):
        admin_user = self.env.ref("base.user_admin")
        demo_user = self.env.ref("base.user_demo").with_user(admin_user)
        rule_record = self.env.ref("access_limit_max_users.max_users_limit")
        rule_record.max_records = self.env["res.users"].search_count(
            [("is_excluded_from_limiting", "=", False)]
        )

        vals = {"is_excluded_from_limiting": True}

        with self.assertRaises(exceptions.ValidationError):
            demo_user.write(vals)

        demo_user.sudo().write(vals)
