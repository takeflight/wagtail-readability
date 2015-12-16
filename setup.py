#!/usr/bin/env python
"""
Install wagtail-readability using setuptools
"""

from wagtailreadability import __version__

with open('README.rst', 'r') as f:
    readme = f.read()

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='wagtail-readability',
    version=__version__,
    description="A plugin to assist with readability in wagtail's hallo.js.",
    long_description=readme,
    author='Liam Brenner',
    author_email='liam@takeflight.com.au',
    url='https://github.com/takeflight/wagtail-readability',

    install_requires=[
        'wagtail>=1.0',
        'textstat>=0.2',
    ],
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)