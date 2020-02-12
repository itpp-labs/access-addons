# -*- coding: utf-8 -*-
from odoo import fields, models


class BaseLimitRecordsNumber(models.Model):
    """Test model to test access"""

    _name = "base.limit.records_number.test"

    name = fields.Char("Name")
