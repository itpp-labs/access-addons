.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

Hide admin from user and partner lists
======================================

Warning
-------

As usual user doesn't see admin user it could lead to ignoring Admin user\partner. E.g. Admin could not get notification, because some mail functions are not executed via sudo. 

Unittests could raise errors, because they assume that admin user is available for other users.

Known issues
============

Non-super users will not be able to update ``one2many`` fields to ``res.users`` model, if Admin is specified in values. In such cases, you have to remove Admin from the field before installing the module. Example: **Team Members** field in ``Sales Team`` model. See https://github.com/it-projects-llc/access-addons/issues/36

Tested on `9.0 <https://github.com/odoo/odoo/commit/2ec9a9c99294761e56382bdcd766e90b8bc1bb38>`_
