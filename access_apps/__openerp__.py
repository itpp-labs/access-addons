# -*- coding: utf-8 -*-
{
    'name': 'Control access to Apps',
    'version': '1.0.1',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'category': 'Access',
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    "license": "LGPL-3",
    'price': 10.00,
    'currency': 'EUR',
    'depends': [
        'web_settings_dashboard',
        'access_restricted'
    ],
    'data': [
        'views/access_apps.xml',
        'security/access_apps_security.xml',
        'security/ir.model.access.csv',
    ],
    "demo": [
    ],
    'installable': True
}
