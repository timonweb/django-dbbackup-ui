#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()


def get_requirements():
    return open('requirements.txt').read().splitlines()

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dbbackup_ui',
    version='0.1.0',
    description="Backup database and media files via Django admin interface (includes Wagtail admin support)",
    long_description=readme + '\n\n' + history,
    author="Tim Kamanin",
    author_email='tim@timonweb.com',
    url='https://github.com/timonweb/dbbackup_ui',
    packages=find_packages(),
    package_dir={'dbbackup_ui':
                 'dbbackup_ui'},
    include_package_data=True,
    install_requires=get_requirements(),
    license="BSD license",
    zip_safe=False,
    keywords=[
        'django', 'database', 'media', 'backup',
        'admin', 'wagtail', 'ui', 'download'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Compression'
    ]
)
