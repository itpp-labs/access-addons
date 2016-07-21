from openerp import models, fields, api, exceptions


class BaseLimitRecordsNumber(models.Model):
    '''Test model to test access'''
    _name = 'base.limit.records_number.test'

    name = fields.Char('Name')
