Basic module for custom security stuff
======================================

The module add checkbox "Custom Group" and puts such access groups to the top of "Access Rights" tab of user form. It helps to manage user roles via creating custom group that is collection of a technical groups.

How to create or edit custom groups:

* open Settings->Users->Groups
* choose some group or create new

  * set checkbox "Custom Group"
  * set Application

To create "Application groups", i.e. it get Selection field in Access Rights tab, groups must belong to the same Application inherit each other.

How to apply groups for some users:

* open Settings->Users->Users
* select user you need
* click "clear access rights"
* tick access groups you need. In the main, you have to use only ones from "Custom User Groups" sector, because all inherited tick boxes will be ticked automatically, after you click save.
* click save

Please note, that if you delete some technical group from custom group, then you have to repeat process of applying groups for each related users. If you don't repeat applying process then removed group would be kept in related users, because there is no way to figure out is it was added by inheritance or manually as a extra access to that user.

*See access_custom module as example of usage.*

Tested on 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d.
