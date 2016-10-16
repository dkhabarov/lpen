lpen.conf.yml 1 "OCTOBER 2015" "" "User Manuals"
=======================================

NAME
----

/etc/lpen/lpen.conf.yml -- Файл настроек для lpen


DESCRIPTION
--------

Файл  /etc/lpen/lpen.conf.yml  содержит  настройки для скрипта lpen. В каждой строке содержится по одному значению в формате параметр: значение. Используется yaml.

Действующие параметры настройки:

`xmpp_login: ` - Логин для авторизации на jabber-сервере

`xmpp_password:` - Пароль для авторизации на jabber-сервере

`user_list_file:`  Файл с пользователями и адресами xmpp/mail

`smtp_server_addr:` - Адрес smtp сервера

`smtp_server_port:` - Порт smtp сервера.

`smtp_auth_user:` - Логин авторизации на сервере

`smtp_auth_password:` - Пароль для авторизции на сервере

`password_expiration_text:` - Текст уведомления, о надобности смены пароля. В тексте можно использовать переменные
`{HOSTNAME}` и `{HOSTNAME}`, которые соответсвенно будут заменены на хостнейм сервера и имя пользователя.

`account_expiration_text:` - Текст уведомления, об истечении срока использования аккаунта. В тексте можно использовать переменные `{HOSTNAME}` и `{HOSTNAME}`, которые соответсвенно будут заменены на хостнейм сервера и имя пользователя.

Файл пользователей: 

```
username:
  jabber: user@xmpp.example.com
  mail: user@example.com
```

AUTHOR
------

Denis Khabarov <admin@saymon21-root.pro>

SEE ALSO
-------
lpen(1), chage(1)

