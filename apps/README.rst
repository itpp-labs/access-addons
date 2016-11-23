=============
 Custom Apps
=============

The module shows only custom apps to user. To use this feature, create some number of modules with prefix ``super_app_`` in technical name (e.g. super_app_pos, super_app_hr, etc). Then a user will be asked to work with applications from that list only and doesn't care about dozen of technical modules, which custom applications consist of.

When user need to uninstall custom app, the module will uninstall dependencies
too. (By default odoo uninstall only modules that depend on the module and
don't touch modules that the module has in dependencies). For example, if we
have following installed custom apps:

* ``super_app_account`` - has in dependencies:

  * ``account``
  * ``account_some_feature``

* ``super_app_pos`` - has in dependencies:

  * ``point_of_sale``
  * ``pos_restaurant``
  * ``inventory``

* ``super_app_sales`` - has in dependencies:

  * ``account``
  * ``sale``
  * ``inventory``
  * ``website_sale``

Then uninstallation scheme is as following:

* ``super_app_account``

  * uninstall ``super_app_account``
  * uninstall ``account_some_feature``

* ``super_app_pos``

  * uninstall ``super_app_pos``
  * uninstall ``point_of_sale``
  * uninstall ``pos_restaurant``

* ``super_app_sales``

  * uninstall ``super_app_sales``
  * uninstall ``sale``
  * uninstall ``website_sale``

Credits
=======

Contributors
------------
* Dinar Gabbasov <gabbasov@it-projects.info>

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`_

Further information
===================

Demo: http://runbot.it-projects.info/demo/access-addons/10.0

HTML Description: https://apps.odoo.com/apps/modules/10.0/apps/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on 10.0 87184d0894fdb7444cc0d4b6e7028f1f97a7c4f7
