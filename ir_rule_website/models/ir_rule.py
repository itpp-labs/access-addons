# -*- coding: utf-8 -*-
import re

from odoo import api, models, tools
from odoo.addons.base.ir.ir_rule import IrRule as IrRuleOriginal
from odoo.osv import expression
from odoo.tools.safe_eval import safe_eval


class IrRule(models.Model):
    _inherit = 'ir.rule'

    @api.model
    def _eval_context(self):
        context = super(IrRule, self)._eval_context()
        context['website_id'] = self._context.get('website_id')
        return context

    @api.model
    @tools.ormcache_context('self._uid', 'model_name', 'mode', keys=["website_id"])
    def _compute_domain(self, model_name, mode="read"):
        return IrRuleOriginal._compute_domain.__wrapped__(self, model_name, mode=mode)

    @api.depends('domain_force')
    def _force_domain(self):
        eval_context = self._eval_context()
        if not eval_context.get('website_id'):
            website_rules = self.filtered(lambda r: re.match(r'.*website_id\s*[)\]].*', r.domain_force))
            for website_rule in website_rules:
                domain_force = re.sub(r"(.*)(\(.*website_id\s*[]]?\s*\))(.*)", r"\1(1, '=', 1)\3", website_rule.domain_force)
                website_rule.domain = expression.normalize_domain(safe_eval(domain_force, eval_context))
            super(IrRule, self - website_rules)._force_domain()
        else:
            super(IrRule, self)._force_domain()
