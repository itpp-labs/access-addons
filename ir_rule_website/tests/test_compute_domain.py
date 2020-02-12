# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase


class TestComputeDomain(TransactionCase):
    at_install = True
    post_install = True

    def setUp(self):
        super(TestComputeDomain, self).setUp()
        self.demo_user = self.env.ref("base.user_demo")
        self.env["ir.rule"].create(
            {
                "name": "test ir_rule_website",
                "model_id": self.env.ref("base.model_res_partner").id,
                "domain_force": "[('parent_id', 'in', [website_id])]",
            }
        )

    def _cached_compute_domain(self, website_id):
        test_domain = ("parent_id", "in", [website_id])
        domain = (
            self.env["ir.rule"]
            .sudo(user=self.demo_user.id)
            .with_context(website_id=website_id)
            ._compute_domain("res.partner")
        )
        self.assertTrue(test_domain in domain)

    def test_cache(self):
        self._cached_compute_domain(1)
        self._cached_compute_domain(2)
