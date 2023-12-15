from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase

GROUP = "base.group_multi_currency"


class TestAllowImplied(TransactionCase):
    def _get_classified_groups(self, config):
        groups = config._get_classified_fields()["group"]
        return [g[0] for g in groups]

    def setUp(self):
        super().setUp()
        self.group = self.env.ref(GROUP)

    def test_base(self):
        demo_user = self.env.ref("base.user_demo")

        group_system = self.env.ref("base.group_system")

        demo_user.write({"groups_id": [(3, self.group.id)]})
        self.group.write({"users": [(3, demo_user.id)]})
        self.assertFalse(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))

        demo_user.write({"groups_id": [(4, group_system.id)]})

        test_config_settings = (
            self.env["res.config.settings"]
            .with_user(demo_user.id)
            .create({"group_test_access_restricted": True})
        )
        self.assertFalse(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))

        # check that the field is readonly
        self.assertTrue(
            test_config_settings.fields_get()["group_test_access_restricted"][
                "readonly"
            ]
        )
        # check that test group hasn't got appended to classified
        self.assertNotIn(
            "self.group", self._get_classified_groups(test_config_settings)
        )

        group_allow = self.env.ref(
            "access_restricted.group_allow_add_implied_from_settings"
        )
        demo_user.write({"groups_id": [(4, group_allow.id)]})

        # check that now the field is not readonly
        self.assertFalse(
            test_config_settings.fields_get()["group_test_access_restricted"][
                "readonly"
            ]
        )
        # check that now the group is in classified
        self.assertIn(
            "group_test_access_restricted",
            self._get_classified_groups(test_config_settings),
        )

        self.assertFalse(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))
        test_config_settings.with_user(demo_user.id).execute()
        self.assertTrue(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))

    def test_assert_raises(self):

        demo_user = self.env.ref("base.user_demo")
        group_system = self.env.ref("base.group_system")

        demo_user.write({"groups_id": [(3, self.group.id)]})
        self.group.write({"users": [(3, demo_user.id)]})
        self.assertFalse(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))

        demo_user.write({"groups_id": [(4, group_system.id)]})
        self.assertFalse(self.env["res.users"].with_user(demo_user.id).has_group(GROUP))

        # check that there is no access to put test group into implied_ids anyways
        with self.assertRaises(AccessError):
            group_system.with_user(demo_user.id).write(
                {"implied_ids": [(4, self.group.id)]}
            )
