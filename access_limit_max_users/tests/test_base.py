# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import exceptions
from odoo.tests import common


@common.tagged("post_install", "-at_install")
class TestBase(common.TransactionCase):
    def test_max_users(self):
        admin_user = self.env.ref("base.user_admin")

        users_count = self.env["res.users"].sudo().search_count([])
        rule_record = self.env.ref("access_limit_max_users.max_users_limit")
        rule_record.max_records = users_count + 1
        max_users_allowed = rule_record.max_records

        Users = self.env["res.users"].sudo(admin_user)

        while users_count < max_users_allowed:
            login = "test_max_users_{}".format(users_count)
            Users.create({"name": login, "login": login})
            users_count += 1

        # limit is reached
        with self.assertRaises(exceptions.UserError):
            login = "test_max_users_{}".format(users_count)
            Users.create({"name": login, "login": login})
