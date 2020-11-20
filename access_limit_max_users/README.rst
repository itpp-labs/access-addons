.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

=======================
 Limit number of users
=======================

With this module you can limit number of users.

This module creates record with external id `access_limit_max_users.max_users_limit`
that defines max amount of users can have current database. By default it is
number of active users at moment of installation of this module.

In order to make user to be ignoring the limit, you can use field ``is_excluded_from_limiting`` in one of the following ways:

* Create or set ``is_excluded_from_limiting`` to True in supersuper (sudo) mode. See `<tests/test_excluded_users.py>`_
* Define user record in `data files <https://www.odoo.com/documentation/13.0/reference/data.html>`__ with ``is_excluded_from_limiting`` set to True.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Eugene Molotov <https://it-projects.info/team/em230418>`__:


Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/13.0/access_limit_max_users/


Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/access_limit_max_users.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/access_limit_max_users.atom>`_

Tested on `Odoo 13.0 <https://github.com/odoo/odoo/commit/991c3392708946fdf9973d18e8c29469fa21eed9>`_
