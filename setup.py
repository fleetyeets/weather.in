#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import weather_in

from os import path
this_directory = path.abspath(path.dirname(__file__)) 
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='weather.in',
    version=weather_in.__version__,
    packages=find_packages(),
    author='fleetyeets',
    author_email='tnp123@protonmail.com',
    description='OpenWeather CLI script',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests',
        'json'
    ],
    url='https://github.com/fleetyeets/weather.in',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: Weather',
    ]
)