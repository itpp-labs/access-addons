=============================
 Limit records of the tables
=============================

Installation
============

Nothing special is needed to install this module.

Usage
=====

* Зайдите в меню ``Settings / Technical / Security / Records Number Limits``
* Создайте новую запись, например:
** Model: res.users
** Domain: [('active', ...)]
** Ограничить количество записей в таблице значением 3
** Создать записи в таблице users
** При превышении будет эксепшн.

Uninstallation
==============

Nothing special is needed to uninstall this module.