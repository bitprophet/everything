#!/usr/bin/env python

from setuptools import setup

import xmlrpclib

client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')

setup(
    name='everything',
    version='0.1.1',
    description='Literally everything',

    author='Jeff Forcier',
    author_email='jeff@bitprophet.org',

    install_requires=client.list_packages(),
)
