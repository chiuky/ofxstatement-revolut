#!/usr/bin/python3
"""Setup
#Note: To publish new version: `./setup.py sdist upload`
"""
import os
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from distutils.core import setup

import unittest

version = "1.0.0"

setup(name='ofxstatement-revolut-italian',
      version=version,
      author="Donato Chiuchiolo",
      author_email="donato.chiuchiolo@gmail.com",
      url="https://github.com/chiuky/ofxstatement-revolut",
      description=("Bank statement parser for Revolut using locale it_IT"),
      long_description=open("README.md").read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      long_description_content_type='text/markdown',
      license="GPLv3",
      keywords=["ofx", "ofxstatement", "banking", "statement", "revolut"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement': [
              'revolut-italian = ofxstatement.plugins.revolut:RevolutPlugin',
          ]
      },
      install_requires=['ofxstatement'],
      extras_require={'test': ["freezegun", "pytest"]},
      include_package_data=True,
      zip_safe=True
      )
