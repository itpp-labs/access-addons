.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

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

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Eugene Molotov <https://it-projects.info/team/em230418>`__:


Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/13.0/database_block/


Notifications on updates: `via Atom <https://github.com/it-projects-llc/access-addons/commits/13.0/database_block.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/access-addons/commits/13.0/database_block.atom>`_

Tested on `Odoo 13.0 <https://github.com/odoo/odoo/commit/03fb98f876ea03deef05acb74144d8e979a61f54>`_
