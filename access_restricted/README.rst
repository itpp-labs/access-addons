.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev


Restricted administration rights
================================

The module hides from an **Internal User** all groups where he is not added to. 
So, he cannot add himself to any **groups** 
and cannot grants other users more access rights than he has himself.

This module adds a special group **'Allow add implied groups from settings'** whose users
can grant other users more access rights by adding them to the same group.

Also using this module, you can restrict access to change some settings of the other modules (e.g. CRM, Sales etc.), 
because modules often make features optional by restricting them to users of certain groups.


Typical usage of the module.
----------------------------

This example requires **access_apps** module `be installed <https://apps.odoo.com/apps/modules/14.0/access_apps/>`_.

- The superuser creates an admin user without any ``Apps Access`` option in its settings. Then the admin has access to settings, but not able to install new apps.


- Without this module, the admin can change the option to ``Apps access: Allow installing apps`` and get access to apps management.




Tested on `Odoo 14.0 <https://github.com/odoo/odoo/commit/c16d4b5e7b9181c2c792f595a117de10510d45be>`_
