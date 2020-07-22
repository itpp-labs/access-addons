.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

=====================
 Database Limit Size
=====================

This module allows blocking backend access when database limit is exceeded

On loading backend page, module fetches size of database (including filestore) and compares it with value, that
is defined in "System Parameters" as ``database_limit_size``. Value is expected to be in bytes.

If ``database_limit_size`` is not given or zero, there is no limit.

Roadmap
=======

* Customize percentage of the limit which, if exceeded, would indicate a warning. As for now it is hardcoded to 90%

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
      at `odoo apps store <https://apps.odoo.com/apps/modules/13.0/database_limit_size/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/13.0

HTML Description: https://apps.odoo.com/apps/modules/13.0/database_limit_size/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/database_limit_size.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/database_limit_size.atom>`_

Tested on Odoo 13.0 41f72d9628b467f82da0fafc15651002a49b10ad
