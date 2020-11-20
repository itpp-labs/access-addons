.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

=============================
Extra access groups for menus
=============================

Menus are visible only for users who are in groups specified in the fields: "groups_id" and "extra_groups_id".

It can be used to temporarily restrict access to menu for all users.
E.g. in Project application only Project Users and Project Managers have access to Project menu. 
Without this module you have to remove these access groups from all users, which means that user hierarchy is lost. 
The module solve this issue.

Usage
=====

The menu record is as follows by default:

::

    <menuitem name="Project" id="base.menu_main_pm" groups="group_project_manager,group_project_user"
        icon="fa-calendar" web_icon="project,static/description/icon.png" sequence="50"/>

Add links to groups in the "extra_groups_id".

::

    <record model='ir.ui.menu' id='base.menu_main_pm'>
        <field name="extra_groups_id" eval="[(4, ref('module_name.group_1')), (4, ref('module_name.group_2'))]"/>
    </record>

Now the "Project" menu is visible only for user who are in the following groups:

(``group_project_manager`` or ``group_project_user``) and (``module_name.group_1`` or ``module_name.group_2``)

This restriction is not applied for admin user.

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* krotov@it-projects.info

Further information
===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/9.0/access_menu_extra_groups/

Tested on `Odoo 9.0 <https://github.com/odoo/odoo/commit/2ec9a9c99294761e56382bdcd766e90b8bc1bb38>`_
