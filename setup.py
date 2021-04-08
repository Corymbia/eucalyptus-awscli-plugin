#!/usr/bin/env python
import sys
from os import path
from setuptools import setup

requires = ['awscli>=1.11.0']

project_dir = path.abspath(path.dirname(__file__))
with open(path.join(project_dir, 'VERSION'), 'rb') as version:
    version = version.read().decode('UTF-8').strip()
with open(path.join(project_dir, 'README.md'), 'rb') as readme:
    long_description = readme.read().decode('UTF-8')

setup(
    name='awscli-plugin-eucalyptus',
    packages=['awscli_plugin_eucalyptus'],
    version=version,
    description='Eucalyptus plugin for AWS CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steve Jones',
    author_email='steve@iaascream.cloud',
    url='https://github.com/corymbia/eucalyptus-awscli-plugin',
    keywords=['awscli', 'eucalyptus'],
    install_requires=requires,
    license='BSD (Simplified)',
    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Internet']
)

