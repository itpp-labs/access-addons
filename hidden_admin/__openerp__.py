# -*- coding: utf-8 -*-
{
    'name': 'Hide admin from user and partner lists',
    'version': '1.0.1',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    "category": "Access",
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    'depends': [
        'mail',
        'ir_rule_protected',
    ],
    'data': [
        'security.xml',
    ],
    'installable': False
}
