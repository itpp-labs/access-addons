{
    'name': 'Control access to Apps',
    'version': '12.0.1.2.0',
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
        'views/res_users_views.xml',
    ],
    "demo": [
    ],
    'installable': False
}
