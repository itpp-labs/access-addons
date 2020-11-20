.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

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

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Ivan Yelizariev <https://www.it-projects.info/team/yelizariev>`__
* `Ildar Nasyrov <https://www.it-projects.info/team/iledarn>`__

===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/10.0/ir_rule_website


Tested on `Odoo 10.0 <https://github.com/odoo/odoo/commit/1ffe85f1cb3defcbf932138e2fc13f3a81b34787>`_
