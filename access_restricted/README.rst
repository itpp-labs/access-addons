Restricted administration rights
================================

The module makes impossible for administrator to set (and see) more access rights (groups) than he already has.
The only partial exception of this rule is made if you are already a member of the 'Allow add implied groups from settings' security group.
Then you are allowed to escalate your privileges but just from ``Settings`` menus (by means of ``group_XXX`` boolean fields of ``res.config.settings`` models views).

This doesn't affect superuser, of course.

Typical usage of the module.
----------------------------

The superuser creates an administrator user without access group "Show Apps Menu" (see **access_apps** module). Then the administrator has access to settings, but not able to install new apps (without this module he can add himself to "Show Apps Menu" and get access to apps).

Tested on 10.0 5f0b7942d551f441aa41e75ee06f2dd163a9c6f6
