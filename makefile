URL := https://github.com/dkhabarov/lpen.git
DEB_PACKAGE_NAME=lpen
MAINTAINER := 'Denis Khabarov <admin@saymon21-root.pro>'
MAINTAINER_HOMEPAGE := http://saymon21-root.pro
DEB_PACKAGE_DESCRIPTION := This script can be used for the notification about of the expiration of the password or account on the server / desktop of GNU/Linux
DEBIAN_KERNEL_CLEANER_VERSION=0.1
PKG_SUBVERSION :=$(shell echo $$((`ls -1 ../../../public/debs|grep -c $DEB_PACKAGE_NAME` + 1 )))

all: download build build_deb


download:
	cd $(CURDIR)/../../../src && \
	test -d ./$(DEB_PACKAGE_NAME) && \
	test -d ./$(DEB_PACKAGE_NAME)/.git && \
	cd ./$(DEB_PACKAGE_NAME) && git pull || git clone $(URL)


build:
	cd $(CURDIR)/../../../src/$(DEB_PACKAGE_NAME) && \
	python setup.py build && \
	python setup.py install --root=$(CURDIR)/../../lpen --install-layout=deb

