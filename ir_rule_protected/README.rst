.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

Protect ir.rule records
=======================

The module allows protect ir.rule from modifying and deleting. Once a rule is marked as protected only superuser is able to control this rule.

Also, the module protect itself from uninstalling by non-superuser.

Roadmap
=======

* The module should allow specifying which admins can switch to superuser mode (set True to all existing admins and False for any new users)

Further information
===================

Tested on `Odoo 14.0 <https://github.com/odoo/odoo/commit/c16d4b5e7b9181c2c792f595a117de10510d45be>`_
