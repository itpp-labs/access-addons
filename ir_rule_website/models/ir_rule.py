# -*- coding: utf-8 -*-

from odoo import api, models, tools, fields
from odoo.addons.base.ir.ir_rule import IrRule as IrRuleOriginal
from odoo.osv import expression
from odoo.tools.safe_eval import safe_eval


class IrRule(models.Model):
    _inherit = 'ir.rule'

    backend_replacement = fields.Selection([
        ("[(1, '=', 1)]", "[(1, '=', 1)]"),
        ("[(0, '=', 1)]", "[(0, '=', 1)]"),
    ], string='Replacement of multi-website rule definition for backend',
        help="""Replacement for multi-website rule when getting access from backend. Leave empty for all other rules.
        (there is usually no 'website_id' value in the rule evaluation context, when using backend).""")

    @api.depends('domain_force')
    def _force_domain(self):
        eval_context = self._eval_context()
        if not eval_context.get('website_id'):
            website_rules = self.filtered(lambda r: r.backend_replacement)
            for rule in website_rules:
                rule.domain = expression.normalize_domain(safe_eval(rule.backend_replacement, eval_context))
            super(IrRule, self - website_rules)._force_domain()
        else:
            super(IrRule, self)._force_domain()

    @api.model
    def _eval_context(self):
        context = super(IrRule, self)._eval_context()
        context['website_id'] = self._context.get('website_id')
        return context

    @api.model
    @tools.ormcache_context('self._uid', 'model_name', 'mode', keys=["website_id"])
    def _compute_domain(self, model_name, mode="read"):
        return IrRuleOriginal._compute_domain.__wrapped__(self, model_name, mode=mode)
