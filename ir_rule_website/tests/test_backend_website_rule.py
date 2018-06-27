# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase


class TestBackendWebsiteRule(TransactionCase):
    at_install = True
    post_install = True

    def setUp(self):
        super(TestBackendWebsiteRule, self).setUp()
        self.user1 = self.env.ref('base.user_demo')
        self.user1.write({
            'backend_website_id': self.env.ref('website.default_website').id,
        })

        model_res_users = self.env.ref('base.model_res_users')
        self.env['ir.rule'].create({
            'name': 'test backend website rule',
            'model_id': model_res_users.id,
            'domain_force': "[('backend_website_id', 'in', [website_id])]",
            'backend_behaviour': 'true',
        })

        User = self.env['res.users']
        self.user2 = User.create({
            'name': 'user2',
            'login': 'user2',
        })
        self.user3 = User.create({
            'name': 'user3',
            'login': 'user3',
            'backend_website_id': self.env.ref('website.default_website').id,
        })

    def test_backend_website_rule(self):
        users = self.env['res.users'].sudo(user=self.user3.id).search([])
        self.assertTrue(self.user2 not in users)
        users = self.env['res.users'].sudo(user=self.user2.id).search([])
        self.assertTrue(self.user2 in users)
