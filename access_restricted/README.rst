.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

=======================
 Restrict Admin rights
=======================

The module makes impossible for Administrator to set (and see) more access rights (groups) than he/she already has.

The only partial exception of this rule is made if you are already a member of the 'Allow add implied groups from settings' security group.

Configuration
=============

You are allowed to escalate your privileges but just from ``Settings`` menus (by means of ``group_XXX`` boolean fields of ``res.config.settings`` models views).

This doesn't affect superuser, of course.

Usage
=====

The superuser creates an administrator user without access group "Show Apps Menu" (see **access_apps** module).

Then the administrator has access to settings, but not able to install new apps (without this module he can add himself to "Show Apps Menu" and get access to apps).

For Odoo versions older than https://github.com/odoo/odoo/commit/5f12e244f6e57b8edb56788147774150e2ae134d check for access rules in the ``write`` method is duplicated with ORM methods, please update Odoo for higher performance

Tested on `Odoo 10.0 <https://github.com/odoo/odoo/commit/49ca43d75cb9a97642c820c2466d454f1ce604cb>`_
