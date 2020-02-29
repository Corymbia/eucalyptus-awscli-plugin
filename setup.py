#!/usr/bin/env python
import sys
from setuptools import setup

requires = ['awscli>=1.11.0']

setup(
    name='awscli-plugin-eucalyptus',
    packages=['awscli_plugin_eucalyptus'],
    version='0.1',
    description='Eucalyptus plugin for AWS CLI',
    author='Steve Jones',
    author_email='steve@iaascream.cloud',
    url='https://github.com/corymbia/eucalyptus-awscli-plugin',
    keywords=['awscli', 'eucalyptus'],
    install_requires=requires,
    license='BSD (Simplified)',
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Simplified BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Internet']
)

