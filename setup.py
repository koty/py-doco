# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~

    setup.py

    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import setup, find_packages

app_name = 'doco'

rst = os.path.join(os.path.dirname(__file__), 'README.rst')
description = ''
with open(rst, 'r') as f:
    description = f.read()

setup(
    name=app_name,
    version='0.0.3',
    author='Shinya Ohyanagi',
    author_email='sohyanagi@gmail.com',
    url='http://github.com/heavenshell/py-doco',
    description='Client library for docomo API written in Python.',
    long_description=description,
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    install_requires=['requests', 'simplejson'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    tests_require=['mock>=1.0.0'],
    test_suite='tests'
)
