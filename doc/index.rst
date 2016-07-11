=============================================
 Limit number of records for arbitrary model
=============================================

Usage
=====

* Open ``Settings / Technical / Security / Records Number Limits`` menu
* Create new recorod. For exapmle:

** Model: Users 
** Domain: [('active', '=', True)]
** Maximum Users: 3

* Save the record
* Try to create more users from ``Settings / Users``. When you try to create more than three users then you see an exception message.
The system doesn't allow you create more than three users.
