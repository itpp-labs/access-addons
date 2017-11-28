=========================
 Limit number of records
=========================

With this module you can limit number of records for any model in specified domain.
For examle, you can restrict number of vehicles in fleet_vehicle, say by three.
If users try to create more then three vehicles then exception occurs.

This module uses base.action.rule to restrict number of records.
And also there is new model base.limit.records_number to strore the settings.

To do new settings to restrict number of records in any model
the user should be a member of ``Control limits on records number`` security group.


Credits
=======

Contributors
------------
* Pavel Romanchenko <romanchenko@it-projects.info>

Sponsors
--------
* `Mattobell <https://www.mattobell.com>`_

Maintainers
-----------
* `IT-Projects LLC <https://it-projects.info>`__

      To get a guaranteed support you are kindly requested to purchase the module at `odoo apps store <https://apps.odoo.com/apps/modules/11.0/access_limit_records_number/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/11.0

HTML Description: https://apps.odoo.com/apps/modules/11.0/access_limit_records_number/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Odoo 11.0 cc031bd2264a7fcd8efbc9105902574111859c8b
