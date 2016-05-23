Restricted administration rights
================================

The module makes impossible for administrator set (and see) more access rights (groups) than he already have.

This doesn't affect superuser, of course.

Typical usage of the module.
----------------------------

The superuser create an administrator user without access group "Show Apps Menu" (see **access_apps** module). Then the administrator have access to settings, but not able to install new apps (without this module he can add himself to "Show Apps Menu" and get access to apps).

Compatibility
-------------

There could be error on installing another module, that update ``base.view_users_form``: ::

    ParseError: "Invalid view definition

    Error details:
    Field `sel_groups_1_2_3` does not exist

In such case open user form for any user or make a call of built-in function ``update_user_groups_view`` before installing new module. See example in ``res_users_clear_access_rights`` module.

Tested on 8.0 0af32f3f84bae07b11abb8538d02e35c7369a348
