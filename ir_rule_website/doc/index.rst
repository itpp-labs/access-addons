===========================
 Multiwebsite in Sec.Rules
===========================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* There is a new setting in each rule now - it is relevant only for website rules with special ``website_id`` parameter in them
* As usual open ``[[ Settings ]] >> Technical >> Security >> Record Rules`` to create a new rule or edit existing one
* You should see on rule form a new group named ``Multi-website extension`` with the ``Backend behaviour`` setting in it
* Leave this field empty if your rule has nothing to do with websites
* Select ``Grant access`` if you want to give access to model from backend, or ``Deny access`` - if you want to restrict
* Note: if you leave this fields empty for a rule that is using ``website_id`` parameter - you may have this kind of error when trying to configure your product's **website_ids** field from odoo backend:

::

 The requested operation cannot be completed due to security restrictions. Please contact your system administrator.

 (Document type: product.template, Operation: read)

from web-interface, or

::

 INFO rw odoo.models: The requested operation cannot be completed due to record rules: Document type: product.template, Operation: read, Records: 47, User: 5

in odoo logs

This is so because in backend rules work in non-website context.
In other words the setting is mandatory for website rules.

Usage
=====

* If you have a model accessible through a website (by means of controller methods) - specify this module into the "depends" section of your manifest file
* Now you can create security rules using `website_id` in `domain_force` fields. For example,

::

 <?xml version="1.0" encoding="utf-8"?>
 <odoo>
   <record id="blog_rule_all" model="ir.rule">
     <field name="name">Blogs available only for specifed websites</field>
     <field name="model_id" ref="model_blog_blog"/>
     <field name="domain_force">[('website_ids', 'in', [website_id])]</field>
     <field name="backend_behaviour">true</field>
   </record>
 </odoo>
