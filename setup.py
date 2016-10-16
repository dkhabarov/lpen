import os
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="lpen",
    version="0.2",
    author="Denis Khabarov",
    author_email="admin@saymon21-root.pro",
    description=("This script can be used for the notification about of the expiration of the password or account on the server / desktop of GNU/Linux."),
    long_description=read('README.md'),
    license="GPLv3",
    keywords="linux passwords security",
    url="https://github.com/dkhabarov/lpen",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "License :: GPL License",
    ],
#    install_requires=[
#        "python-xmpp",
#        "python-yaml"
#    ],
    entry_points = {
        'console_scripts': ['lpen=lpen.lpen:main'],
    },
    requires=["xmpppy","pyyaml"],
)
