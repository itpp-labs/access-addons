.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

=====================
 Database expiration
=====================

With this module you can make database to expire.

After reaching expiration date "Your database is expired" will be shown.
Expiration date is defined in "System Parameters" as `database_expiration_date`.

Also if ``web_responsive`` is installed, 7 days before expiration date
module will start to show warning in main menu.
To configure how many days to show warning in advance, you can set ``database_expiration_warning_delay`` in "System Parameters"

You can also add hyperlink below warning/expiration message. To define url, set ``database_expiration_details_link`` in "System Parameters".
By default hyperlink's label is "Details". To define the other one, set ``database_expiraation_details_link_label`` in "System Paramters".

Credits
=======

Contributors
------------
* `Eugene Molotov <https://it-projects.info/team/em230418>`__:

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`__

Maintainers
-----------
* `IT-Projects LLC <https://it-projects.info>`__

      To get a guaranteed support
      you are kindly requested to purchase the module
      at `odoo apps store <https://apps.odoo.com/apps/modules/13.0/database_expiration/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/13.0

HTML Description: https://apps.odoo.com/apps/modules/13.0/database_expiration/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/database_expiration.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/database_expiration.atom>`_

Tested on Odoo 12.0 6a57ad66b8374966ba7011e34cec20f6344f4f6d
