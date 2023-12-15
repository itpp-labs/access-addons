==================================
 Restricted administration rights
==================================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============


* `Log in as SUPERUSER <https://odoo-development.readthedocs.io/en/latest/odoo/usage/login-as-superuser.html>`__
* Navigate to menu ``[[ Settings  ]] >> Users & Companies >> Users``
* In ``Access Rights`` tab you can select *Allow add implied groups from settings*:
  it allows a user to configure groups via ``group_XXX`` fields from ``Settings`` menu.

Usage
=====

By default all users except a superuser restricted to escalate the privileges.

Let's take ``Sales (sale_management)`` module as an example.

Without this module installed:

* Say you have a user with administration rights ``Administration: Access Rights``. This user thus may increase his own rights in ``Application Accesses`` from ``Sales: User: Own Documents Only``
  to ``Sales: Administrator``. Also he can open menu ``[[ Sales ]] >> Configuration >> Settings`` and select ``Customer Addresses`` there
  and then click ``[Apply]`` button (adding ``group_sale_delivery_address``)

With this module installed:

* The user from previous example cannot increase his privileges. There is no ``Sales: Manager`` option for him, and also no ``Customer Addresses``
  option in module configuration
* The only exception is done for users who are in special group *Allow add implied groups from settings*: if your user is included in this group by the superuser then you may select
  ``Customer Addresses`` from ``Sale`` module ``Configuration >> Settings`` menu
