# Copyright 2020 Ivan Yelizariev
# License MIT (https://opensource.org/licenses/MIT).
from odoo import api, models


class IrRule(models.Model):
    _inherit = "ir.rule"

    @api.model
    def _eval_context(self):
        context = super(IrRule, self)._eval_context()
        context["website_ids"] = self.env.context.get("allowed_website_ids", [])
        context["websites"] = self.env["website"].browse(context["website_ids"])
        return context

    def _compute_domain_keys(self):
        """ Return the list of context keys to use for caching ``_compute_domain``. """
        return super(IrRule, self)._compute_domain_keys() + ["allowed_website_ids"]
