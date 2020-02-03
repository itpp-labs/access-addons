=======================
 Restrict admin rights
=======================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* By default all users except a superuser restricted to escalate the privileges
* There is only one configuration option this module provides. Open menu ``[[ Settings  ]] >> Users >> Users``
* In ``Access Rights`` tab you can select 'Allow add implied groups from settings' -
  to allow some users to configurate modules by means of ``group_XXX`` fields from ``Settings`` menus

Usage
=====

Let's take ``Sale`` module as an example.

Without this module installed:

* Say you have a user with administration rights ``Administration: Access Rights``. This user thus may increase his own rights in ``Application > Sales`` from ``Sales: User: All Documents``
  to ``Sales: Manager``. Also he can open menu ``[[ Sales ]] >> Configuration >> Settings`` and select ``Display 3 fields on sales orders: customer, invoice address, delivery address`` there
  and then click ``[Apply]`` button (adding ``group_sale_delivery_address``)

With this module installed:

* The user from previous example cannot increase his privileges. There is no ``Sales: Manager`` option for him, and also no ``Display 3 fields on sales orders: customer, invoice address, delivery address``
  option in mudule configuration
* The only exception is done for users who are in special group 'Allow add implied groups from settings' - if your user is included in this group by the superuser then you may select
  ``Display 3 fields on sales orders: customer, invoice address, delivery address`` from ``Sale`` module ``Configuration >> Settings`` menu
