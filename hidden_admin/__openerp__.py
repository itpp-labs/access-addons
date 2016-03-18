{
    'name': 'Hide admin from user and partner lists',
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'category': 'Tools',
    'website': 'https://twitter.com/yelizariev',
    'depends': [
        'mail', # we need this dependency to avoid test errors on --test-enabled
        'ir_rule_protected',
    ],
    'data': [
        'security.xml',
    ],
    'installable': True
}
