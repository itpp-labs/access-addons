Control access to Apps
======================

There are two use cases of this module:

* In Odoo all members of security group ``Administration: Settings`` (``base.group_system``) have rights to install additional modules.
  But what if you want to restrict such access even for them?

* You have a user you want to permit application installation to. But you don't want him to have all rights that members of the ``Administration: Settings`` group have.

There is even third specific case -  when you want to restrict application installation but leave the ability to install apps from ``Configuration >> Settings``
(as you know some addons inherit `res.config.settings` allowing to add features by means of installation additional modules)

Tested on 10.0 5f0b7942d551f441aa41e75ee06f2dd163a9c6f6
