=====================
 Database expiration
=====================

Installation
============
* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* `Log in as admin
* `Activate Developer Mode <https://odoo-development.readthedocs.io/en/latest/odoo/usage/debug-mode.html>`__
* Open menu ``[[ Settings ]] >> Technical >> System Parameter``
* Edit existing record by key `database_expiration_date` or create new one
* Set date with format YYYY-MM-DD HH:MM:SS, click "Save" and reload web page
* If you set past date, "Your database is expired" will appear and will disable navigating
* If you set future date in range of 7 days and you have installed `web_responsive` module installed, you will see warning message in main menu page
