# -*- coding: utf-8 -*-

from odoo import api, models, tools
from odoo.addons.base.ir.ir_rule import IrRule as IrRuleOriginal


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
