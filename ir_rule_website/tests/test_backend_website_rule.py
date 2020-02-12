# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase


class TestBackendWebsiteRule(TransactionCase):
    at_install = True
    post_install = True

    def setUp(self):
        super(TestBackendWebsiteRule, self).setUp()
        self.website1 = self.env.ref("website.default_website")
        self.website2 = self.env.ref("website.website2")
        self.user1 = self.env.ref("base.user_demo")
        self.user1.write(
            {"backend_website_id": self.env.ref("website.default_website").id}
        )

        model_res_users = self.env.ref("base.model_res_users")
        self.env["ir.rule"].create(
            {
                "name": "test backend website rule",
                "model_id": model_res_users.id,
                "domain_force": "[('backend_website_id', 'in', [website_id])]",
                "backend_behaviour": "true",
            }
        )

        User = self.env["res.users"]
        self.user2 = User.create({"name": "user2", "login": "user2"})
        self.user3 = User.create(
            {
                "name": "user3",
                "login": "user3",
                "backend_website_id": self.env.ref("website.default_website").id,
            }
        )

        # case for an object references another object
        # e.g. [('id','=', website.company_id.id)]
        model_res_company = self.env.ref("base.model_res_company")
        company2_partner = self.env["res.partner"].create(
            {"name": "Partner for Comapny2", "is_company": True}
        )
        self.company1 = self.env.ref("base.main_company")
        self.company2 = self.env["res.company"].create(
            {
                "name": "Test Company2",
                "partner_id": company2_partner.id,
                "parent_id": False,
            }
        )
        self.website2.company_id = self.company2.id
        self.env["ir.rule"].create(
            {
                "name": "test website references company",
                "model_id": model_res_company.id,
                "domain_force": "[('id','=', website.company_id.id)]",
                "backend_behaviour": "false",
                "groups": [(6, 0, [self.env.ref("base.group_user").id])],
            }
        )

    def test_backend_website_rule(self):
        users = self.env["res.users"].sudo(user=self.user3.id).search([])
        self.assertTrue(self.user2 not in users)
        users = self.env["res.users"].sudo(user=self.user2.id).search([])
        self.assertTrue(self.user2 in users)

        # case when in a rule the `website` object references another object (`res.company` in that case)
        companies = self.env["res.company"].sudo(user=self.user1.id).search([])
        self.assertFalse(self.company2 in companies)
        self.assertNotIn(self.company2, companies)
        with self.assertRaises(AccessError):
            self.env["res.company"].sudo(user=self.user1.id).browse(
                self.company2.id
            ).name

        companies = (
            self.env["res.company"]
            .sudo(user=self.user1.id)
            .with_context(website_id=self.website2.id)
            .search([])
        )
        self.assertIn(self.company2, companies)
        name = (
            self.env["res.company"]
            .sudo(user=self.user1.id)
            .with_context(website_id=self.website2.id)
            .browse(self.company2.id)
            .name
        )
        self.assertEqual(name, self.company2.name)
