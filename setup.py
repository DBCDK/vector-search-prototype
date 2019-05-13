#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
from setuptools import setup, find_packages

## See the following pages for keywords possibilities for setup keywords, etc.
# https://packaging.python.org/
# https://docs.python.org/3/distutils/apiref.html
# https://docs.python.org/3/distutils/setupscript.html

setup(name='vector-search',
      version='0.1.0',
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      description='prototype of vector-search (lsa)',
      test_suite='vector_search.tests',
      provides=['vector_search'],
      maintainer="shm",
      maintainer_email="shmollerup@gmail.com",
      zip_safe=False)
