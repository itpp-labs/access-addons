.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

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
* Website rules don't work for ``/mail/read_followers`` method: https://github.com/itpp-labs/access-addons/issues/232

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* `Ivan Yelizariev <https://www.it-projects.info/team/yelizariev>`__
* `Ildar Nasyrov <https://www.it-projects.info/team/iledarn>`__

===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/13.0/ir_rule_website


Tested on `Odoo 13.0 <https://github.com/odoo/odoo/commit/669203b6a86c1c2d8463dc34b8674b2a38010ed0>`_
