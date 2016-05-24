{
    'name': 'Hide admin from user and partner lists',
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'category': 'Tools',
    'website': 'https://twitter.com/yelizariev',
    'depends': [
        'mail',
        'ir_rule_protected',
    ],
    'data': [
        'security.xml',
    ],
    'post_load': 'post_load',
    'installable': True
}
