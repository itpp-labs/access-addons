Restricted administration rights
================================

The module makes impossible for administrator set (and see) more access rights (groups) than he already have.

This doesn't affect superuser, of course.

Typical usage of the module.
----------------------------

The superuser create an administrator user without access group "Show Apps Menu" (see **access_apps** module). Then the administrator have access to settings, but not able to install new apps (without this module he can add himself to "Show Apps Menu" and get access to apps).

Tested on 10.0 1be57f2825af4f3ade20a658c6f97f6cf93cc866
