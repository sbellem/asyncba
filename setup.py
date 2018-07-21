#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup, find_packages

NAME = 'asyncba'
DESCRIPTION = 'asyncba'
URL = 'https://github.com/sbellem/asyncba'
EMAIL = 'sbellem@gmail.com'
AUTHOR = 'Sylvain Bellemare'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
)
