=========================================
 Multi-website support in Security Rules
=========================================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

This is a core technical module - no configurations are needed

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
   </record>
 </odoo>
