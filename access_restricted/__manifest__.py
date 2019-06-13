{
    'name': 'Restricted administration rights',
    'version': '12.0.1.3.5',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    "category": "Access",
    "support": "apps@it-projects.info",
    'website': 'https://apps.odoo.com/apps/modules/12.0/access_restricted/',
    "license": "LGPL-3",
    'price': 30.00,
    'currency': 'EUR',
    'depends': ['ir_rule_protected'],
    'data': [
        'security/access_restricted_security.xml',
    ],
    'installable': True
}
