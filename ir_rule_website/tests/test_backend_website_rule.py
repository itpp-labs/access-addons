# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase


class TestBackendWebsiteRule(TransactionCase):
    at_install = True
    post_install = True

    def setUp(self):
        super(TestBackendWebsiteRule, self).setUp()
        self.demo_user = self.env.ref('base.user_demo')
        self.demo_user.write({
            backend_website_id: self.enf.ref('website.default_website').id,
        }

        model_res_partner = self.env.ref('base.model_res_partner')
        self.env['ir.rule'].create({'name': 'test backend website rule',
                                    'model_id': model_res_partner.id,
                                    'domain_force': "[('parent_id', 'in', [website_id])]"})

    def _cached_compute_domain(self, website_id):
        test_domain = ('parent_id', 'in', [website_id])
        domain = self.env['ir.rule'].sudo(user=self.demo_user.id)._compute_domain('res.partner')
        self.assertTrue(test_domain in domain)

    def test_backend_website_rule(self):
        self._cached_compute_domain(self.enf.ref('website.default_website').id)
