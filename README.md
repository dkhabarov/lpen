# lpen

Данный скрипт предназначен для уведомления об истечении срока использования пароля или аккаунта на сервере/десктопе под GNU/Linux Для начала нужно установить модули к python.

Debian/Ubuntu:

`aptitude -y install python-xmpp python-yaml`

CentOS: Для начала нужно подключить репозиторий rpmforge. Как это сделать, читайте тут: http://wiki.centos.org/AdditionalResources/Repositories/RPMForge Как подключили, ставим модули:

`yum -y install python-xmpp python-yaml`

Calculate Linux/Gentoo:

```shell

emerge dev-python/xmpppy
emerge dev-python/pyyaml
```
Установить дату использования пароля:

`chage -M 40 --inactive -1 --warndays 5 sysusername`

Скопировать конфиг файлы в /etc

```shell
cp lpen.conf.yaml /etc/lpen.conf.yaml 
cp .linux_pass_expire_users.yaml /etc/.linux_pass_expire_users.yaml
```

Отредактировать /etc/lpen.conf.yaml, указать данные для авторизации на xmpp/smtp-сервере, которые будет использован для отправки уведомлений. Отредактировать /etc/.linux_pass_expire_users.yaml, указать юзеров, для которых надо отправлять уведомления, и так-же указать их xmpp/email адреса.

Обязательно надо дать скрипту права на исполнение chmod +x ну и забиваем в крон на любое удобное для вас время.

**Внимание!** Скрипт должен выполнятся от рута или любого другого юзера, который имеет права на чтение /etc/shadow!!!!
