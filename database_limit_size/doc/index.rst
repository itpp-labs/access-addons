=====================
 Database Limit Size
=====================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* `Log in as admin
* `Activate Developer Mode <https://odoo-development.readthedocs.io/en/latest/odoo/usage/debug-mode.html>`__
* Open menu ``[[ Settings ]] >> Technical >> System Parameter``
* Edit existing record by key ``database_limit_size`` or create new one
* Set integer value, click "Save" and reload web page
* If you set small nonzero value (for example "1" without quotes), "Database size exceed" will appear and will disable navigating
* If you set value that is less than actual database size, but greater than 90% of actual database size and ``web_responsive`` is installed, you will see warning message "Database size is about to be exceed"
