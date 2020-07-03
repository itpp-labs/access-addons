# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import exceptions
from odoo.tests import common


@common.tagged("post_install", "-at_install")
class TestBase(common.TransactionCase):
    def _test_max_users(self, create_excluded_user=False):
        admin_user = self.env.ref("base.user_admin")

        users_count = self.env["res.users"].sudo().search_count([])
        rule_record = self.env.ref("access_limit_max_users.max_users_limit")
        rule_record.max_records = users_count + 1
        max_users_allowed = rule_record.max_records

        Users = self.env["res.users"].with_user(admin_user)

        while users_count < max_users_allowed:
            login = "test_max_users_{}".format(users_count)
            Users.create({"name": login, "login": login})
            users_count += 1

        if create_excluded_user:
            login = "test_excluded_user"
            Users.sudo().create(
                {"name": login, "login": login, "is_excluded_from_limiting": True}
            )

        # limit is reached
        with self.assertRaises(exceptions.UserError):
            login = "test_max_users_{}".format(users_count)
            Users.create({"name": login, "login": login})

    def test_max_users(self):
        self._test_max_users(create_excluded_user=False)

    def test_max_users_with_excluded(self):
        self._test_max_users(create_excluded_user=True)
