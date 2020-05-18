# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).
from odoo.tests import common


@common.tagged("post_install", "-at_install")
class TestBase(common.TransactionCase):
    def test_max_users(self):
        admin_user = self.env.ref("base.user_admin")

        users_count = self.env["res.users"].sudo().search_count([])
        max_users_allowed = self.env.ref(
            "access_limit_max_users.max_users_limit"
        ).max_records

        Users = self.env["res.users"].with_user(admin_user)

        while users_count < max_users_allowed:
            Users.create({"name": "test_max_users_{}".format(users_count)})
            users_count += 1

        # limit is reached
        with self.assertRaises(Exception):
            Users.create({"name": "test_max_users_{}".format(users_count)})
