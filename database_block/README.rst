.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

==================
 Block backend UI
==================

This technical module allows blocking backend access and display the message

In order to do that, dependent module need to override ``ir.http`` 's session_info method and return
dictionary with following keys:

* ``database_block_message`` - the displayed message itself. Can be HTML
* ``database_block_is_warning`` - if true, backend is not blocked, but displayed message is shown as warning (``web_responsive`` must be installed in order for warning to be displayed)

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
      at `odoo apps store <https://apps.odoo.com/apps/modules/13.0/database_block/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/13.0

HTML Description: https://apps.odoo.com/apps/modules/13.0/database_block/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/database_block.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/database_block.atom>`_

Tested on Odoo 13.0 03fb98f876ea03deef05acb74144d8e979a61f54
