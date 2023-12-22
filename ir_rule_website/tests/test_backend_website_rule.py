# Copyright 2020 Ivan Yelizariev
# License MIT (https://opensource.org/licenses/MIT).
from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase

# TODO: the tests are quick fixes of the tests for 1.x.x version and need to be cleanup


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
                "domain_force": "[('backend_website_id', 'in', website_ids)]",
            }
        )

        User = self.env["res.users"]
        self.user2 = User.create(
            {"name": "user2", "login": "user2", "backend_website_id": self.website1.id}
        )
        self.user3 = User.create(
            {"name": "user3", "login": "user3", "backend_website_id": self.website2.id}
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
                "name": "test websites references company",
                "model_id": model_res_company.id,
                "domain_force": "[('id','=', websites[0].company_id.id)]",
            }
        )

    def test_backend_website_rule(self):
        users = (
            self.env["res.users"]
            .with_user(self.user1)
            .with_context(allowed_website_ids=[self.website1.id])
            .search([])
        )
        self.assertIn(self.user2, users)
        self.assertNotIn(self.user3, users)
        users = (
            self.env["res.users"]
            .with_user(self.user1)
            .with_context(allowed_website_ids=[self.website2.id])
            .search([])
        )
        self.assertNotIn(self.user2, users)
        self.assertIn(self.user3, users)

        # case when in a rule the `website` object references another object (`res.company` in that case)
        companies = (
            self.env["res.company"]
            .with_user(self.user1)
            .with_context(allowed_website_ids=[self.website1.id])
            .search([])
        )
        self.assertNotIn(self.company2, companies)
        self.env["res.company"].invalidate_cache()
        with self.assertRaises(AccessError):
            (
                self.env["res.company"]
                .with_user(self.user1)
                .with_context(allowed_website_ids=[self.website1.id])
                .browse(self.company2.id)
                .name
            )

        self.env["res.company"].invalidate_cache()
        self.user1.write(
            {"company_id": self.company2.id, "company_ids": [(4, self.company2.id, 0)]}
        )
        companies = (
            self.env["res.company"]
            .with_user(self.user1)
            .with_context(allowed_website_ids=[self.website2.id])
            .search([])
        )
        self.assertIn(self.company2, companies)
        name = (
            self.env["res.company"]
            .with_user(self.user1)
            .with_context(allowed_website_ids=[self.website2.id])
            .browse(self.company2.id)
            .name
        )
        self.assertEqual(name, self.company2.name)
