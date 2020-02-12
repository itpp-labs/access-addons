# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models
from odoo.tools.safe_eval import safe_eval
from odoo.tools.translate import _


class BaseLimitRecordsNumber(models.Model):
    _name = "base.limit.records_number"
    _inherits = {"base.action.rule": "action_rule_id"}

    action_rule_id = fields.Many2one(
        "base.action.rule", "Base Action Rule", required=True, ondelete="cascade"
    )
    max_records = fields.Integer(string="Maximum Records")
    domain = fields.Char(string="Domain", default="[]")

    @api.model
    def default_get(self, default_fields):
        res = super(BaseLimitRecordsNumber, self).default_get(default_fields)
        res["kind"] = "on_create_or_write"
        return res

    @api.model
    def create(self, vals):
        record = super(BaseLimitRecordsNumber, self).create(vals)
        server_actions_ids = [
            (
                4,
                self.env.ref(
                    "access_limit_records_number.action_check_records_number"
                ).id,
                False,
            )
        ]
        record.write({"server_action_ids": server_actions_ids})
        return record

    @api.model
    def verify_table(self):
        """ Get parameters and verify. Raise exception if limit """
        model_name = self.env.context["active_model"]
        for rule in self.search([("model_id.model", "=", model_name)]):
            records_count = self.env[model_name].search_count(safe_eval(rule.domain))
            if records_count > rule.max_records:
                raise exceptions.Warning(
                    _(
                        'Maximimum allowed records in table "%(model_name)s" is %(max_records)s, while after this update you would have %(records_count)s'
                    )
                    % {
                        "model_name": rule.model_id.name,
                        "max_records": rule.max_records,
                        "records_count": records_count,
                    }
                )
