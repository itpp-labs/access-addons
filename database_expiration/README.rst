.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

=====================
 Database expiration
=====================

With this module you can make database to expire.

After reaching expiration date a 'Your database is expired!' message will be shown.

In order to do that, dependent module need to override ``ir.http`` 's ``session_info``
method and return dictionary with following keys:

* ``database_expiration_date`` - this parameter record the date time value like **YYYY-MM-DD HH:MM:SS**,
  for example, '2021-12-01 13:45:00'.

* ``database_expiration_warning_delay`` - this parameter record a integer value for how many days
  to show warning in advance, for example, **5**, it use by as default value: *7*.

* ``database_expiration_details_link`` - this parameter record a text value for add hyperlink below
  warning/expiration message, for example, **https://support.mystore.com/**.

* ``database_expiration_details_link_label`` - this parameter record a text value for the hyperlink's
  label for the link, for example, **More details**, it use by as default value: *Details*.

For setup this add-on is defined in "Settings > Technical > Parameters > System Parameters".

Also if ``web_responsive`` add-on is installed, by default 7 days before expiration date 
module will start to show warning in main menu.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Eugene Molotov <https://it-projects.info/team/em230418>`__:


Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/13.0/database_expiration/


Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/database_expiration.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/database_expiration.atom>`_

Tested on `Odoo 13.0 <https://github.com/odoo/odoo/commit/6a57ad66b8374966ba7011e34cec20f6344f4f6d>`_
