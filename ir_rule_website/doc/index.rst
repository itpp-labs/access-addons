==========================
 Multi-Brand Access Rules
==========================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Backend Usage
=============

* As usual open ``[[ Settings ]] >> Technical >> Security >> Record Rules`` to create a new rule or edit existing one
* RESULT: you can use variables ``websites`` and ``website_ids`` in **domain_force** field

Usage in a module
=================

If you have a model accessible through a website, you can apply restriction in a following way:

* Add field ``website_ids`` to your model to specify on which websites the record should be available
* Add this ``ir_rule_website`` into the ``"depends"`` section of your manifest file
* Create a security  rule using ``website_ids`` in ``domain_force`` field. For example,

::

 <?xml version="1.0" encoding="utf-8"?>
 <odoo>
   <record id="blog_rule_all" model="ir.rule">
     <field name="name">Blogs available only for specifed websites</field>
     <field name="model_id" ref="model_blog_blog"/>
     <field name="domain_force">[('website_ids', 'in', website_ids)]</field>
   </record>
 </odoo>
