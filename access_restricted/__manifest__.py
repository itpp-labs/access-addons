# -*- coding: utf-8 -*-
{
    'name': 'Restrict Admin rights',
    'version': '10.0.1.3.4',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    "category": "Access",
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    'images': ['images/access_restricted.jpg'],
    "license": "LGPL-3",
    'price': 30.00,
    'currency': 'EUR',
    'depends': ['ir_rule_protected'],
    'data': [
        'security/access_restricted_security.xml',
    ],
    'installable': True
}
