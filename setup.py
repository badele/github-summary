#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return open(path).read()


setup(
    name='github-summary',
    version='0.1.0-dev',
    description='Python tool for generate github summary in multiple formats',
    long_description=read('README.rst'),
    author='Bruno Adelé',
    author_email='bruno@adele.im',
    url='https://github.com/badele/github-summary',
    license='GPL',
    install_requires=[
        'jinja2',
        'pygithub',
    ],
    setup_requires=[],
    tests_require=['python-coveralls'],
    test_suite='tests',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['githubsummary/tools/org2json'],
    entry_points={
        'console_scripts': [
            'githubsummary = githubsummary.githubsummary:main',
        ],
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
