#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from encrypted_cookiejar import __version__

install_requires = [line.rstrip() for line in open(os.path.join(os.path.dirname(__file__), 'requirements.txt'))]

setup(name='encrypted_cookiejar',
      version=__version__,
      description='Fernet-encrypted cookie jar',
      long_description='python-encrypted-cookiejar is a Python library for storing cookie jar encrypted with Fernet.',
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      keywords='cookiejar',
      author='Andrea Bonomi',
      author_email='andrea.bonomi@gmail.com',
      url='http://github.com/andreax79/python-encrypted-cookiejar',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points={},
      test_suite='test',
      tests_require=['nose'])
