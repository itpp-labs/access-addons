# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
from odoo.tests import common


@common.tagged("post_install", "-at_install")
class TestBase(common.TransactionCase):
    def test_users(self):
        demo_user = self.env.ref("base.user_demo")

        # ok
        self.env["base.limit.records_number.test"].with_user(demo_user).create(
            {"name": "r1"}
        )

        # limit 1 is reached
        with self.assertRaises(Exception):
            self.env["base.limit.records_number.test"].with_user(demo_user).create(
                {"name": "r2"}
            )

    def test_set_max_records(self):
        max_records = 3
        self.env["base.limit.records_number"].set_max_records(
            "access_limit_records_number.test_rule", max_records
        )

        demo_user = self.env.ref("base.user_demo")

        # ok
        for i in range(3):
            self.env["base.limit.records_number.test"].sudo(demo_user).create(
                {"name": "r{}".format(i)}
            )

        # limit 1 is reached
        with self.assertRaises(Exception):
            self.env["base.limit.records_number.test"].sudo(demo_user).create(
                {"name": "r{}".format(max_records)}
            )
