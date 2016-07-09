#!/usr/bin/env python

from setuptools import setup
#from distutils.core import setup

setup(name='displayname',
      version='0.1.0',
      description='Getting user name for display',
      long_description='''
It gets user name for display ("First Family") from operating system.

It is a FullName on Windows, RealName on macOS.

This is a multi-platform and a pure Python library.
''',
      author='Yoshiki Shibukawa',
      author_email='yoshiki at shibu.jp',
      url='https://github.com/shibukawa/displayname_py',
      license="MIT",
      py_modules=['displayname'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: PyPy'
     ]
)
