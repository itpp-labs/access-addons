Hide admin from user and partner lists
======================================

Warning
-------

As usual user doesn't see admin user it could lead to ignoring Admin user\partner. E.g. Admin could not get notification, because some mail functions are not executed via sudo. 

Unittests could raise errors, because they assume that admin user is available for other users.

Tested on 9.0 2ec9a9c99294761e56382bdcd766e90b8bc1bb38
