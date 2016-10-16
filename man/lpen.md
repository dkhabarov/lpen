lpen 1 "OCTOBER 2015" "" "User Manuals"
=======================================

NAME
----

lpen -- Скрипт, позволяющий отсылать уведомления об истечении срока использования пароля или аккаунта.


DESCRIPTION
--------

Скрипт, позволяющий отсылать уведомления об истечении срока использования пароля или аккаунта.

FILES
-----
*/etc/lpen/lpen.conf.yml*
Оновные настройки

*/etc/lpen/linux_pass_expire_users.yaml*
Cписок пользоватеей их email/xmpp адреса


NOTES
------

Скрипт должен иметь права для чтения файла `/etc/shadow`

Для работы нужно добавить задачу в crontab(1)


AUTHOR
------

Denis Khabarov <admin@saymon21-root.pro>

SEE ALSO
-------
lpen.conf(1), chage(1)

