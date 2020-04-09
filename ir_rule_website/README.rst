==========================
 Multi-Brand Access Rules
==========================

Allows to use new variables to be used in ``domain_force`` field of Record Rules (``ir.rule``):

* ``website_ids`` -- equal to ``context["allowed_website_ids"]`` (see module ``web_website``)
* ``websites`` -- browsed ``website_ids``

For your information: Odoo provides ``website`` variable, which is equal to current website in frontend and is empty in backend

Example of usage:

* Show a blog on specific websites only (TODO: add link to the module)
* Show an event on specific websites only (TODO: add link to the module)
* Show a product on specific websites only (TODO: add link to the module)

Roadmap
=======

* This module can be merged to ``web_website`` module

Credits
=======

Contributors
------------
* `Ivan Yelizariev <https://www.it-projects.info/team/yelizariev>`__
* `Ildar Nasyrov <https://www.it-projects.info/team/iledarn>`__

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`__

Maintainers
-----------
* `IT-Projects LLC <https://it-projects.info>`__

      To get a guaranteed support you are kindly requested to purchase the module at `odoo apps store <https://apps.odoo.com/apps/modules/13.0/ir_rule_website/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/13.0

HTML Description: https://apps.odoo.com/apps/modules/13.0/ir_rule_website

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Odoo 13.0 669203b6a86c1c2d8463dc34b8674b2a38010ed0
