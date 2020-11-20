.. image:: https://itpp.dev/images/infinity-readme.png
   :alt: Tested and maintained by IT Projects Labs
   :target: https://itpp.dev

Restricted administration rights
================================

The module makes impossible for administrator set (and see) more access rights (groups) than he already have.

This doesn't affect superuser, of course.

Typical usage of the module.
----------------------------

The superuser create an administrator user without access group "Show Apps Menu" (see **access_apps** module). Then the administrator have access to settings, but not able to install new apps (without this module he can add himself to "Show Apps Menu" and get access to apps).

Tested on `8.0 <https://github.com/odoo/odoo/commit/0af32f3f84bae07b11abb8538d02e35c7369a348>`_
