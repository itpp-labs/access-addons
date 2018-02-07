=========================================
 Multi-website support in Security Rules
=========================================

Allows to use ``website_id`` (current website) in ``domain_force`` field of Record Rules (``ir.rule``), e.g.:

* ``[('website_ids', 'in', [website_id])]``
* ``[('website_id', '=', website_id)]``


Example of usage: 

* Show a blog on specific websites only (TODO: add link to the module)
* Show an event on specific websites only (TODO: add link to the module)
* Show a product on specific websites only (TODO: add link to the module)

Odoo 12.0+
==========

We hope this feature will be built-in since Odoo 12.0 at least: https://github.com/odoo/odoo/pull/22743

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

      To get a guaranteed support you are kindly requested to purchase the module at `odoo apps store <https://apps.odoo.com/apps/modules/11.0/ir_rule_website/>`__.

      Thank you for understanding!

      `IT-Projects Team <https://www.it-projects.info/team>`__

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/11.0

HTML Description: https://apps.odoo.com/apps/modules/11.0/ir_rule_website

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Odoo 11.0 dc61861f90d15797b19f8ebddfb0c8a66d0afa88
