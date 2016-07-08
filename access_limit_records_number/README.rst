=============================
 Limit records of the tables
=============================

Приложение предоставляет возможность ограничить количество записей в любой таблице. Осуществляется путем установки правил в моделе base.actions.rule. Настройки ограничений для каждой таблицы делаются в новой моделе base.limit.records_number.

При создании или обновлении записи происходит проверка првышен ли лимит. Если лимит первышен, будет вызываться эксепшн.

Изменять правила и менять настройки могут только те, у кого есть на это доступ. Этот доступ предоставляется для пользователя, который имеет доступ Control Records Number Limits.

Credits
=======

Contributors
------------
* Pavel Romanchenko <romanchenko@it-projects.info>

Sponsors
--------
* `IT-Projects LLC <https://it-projects.info>`_

Further information
===================

.. Demo: http://runbot.it-projects.info/demo/REPO-NAME/BRANCH

HTML Description: https://apps.odoo.com/apps/modules/9.0/access_limit_records_number/

Usage instructions: `<doc/index.rst>`_

Changelog: `<doc/changelog.rst>`_

Tested on Odoo 9.0 b9bca7909aee5edd05d1cf81d45a540b7856f76e