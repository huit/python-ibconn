from setuptools import setup, find_packages
import sys, os

long_description = 'IBConn is a library for working with the infoblox rest api'
version = '0.1'

setup(
    name='ibconn',
    version=version,
    description="infoblox client library",
    long_description=long_description,
    url='http://github.com/huit/python-ibconn',
    keywords='infoblox',
    author='Luke Sullivan',
    author_email='luke_sullivan@harvard.edu',
    license='MIT',
    packages=['ibconn'],
    install_requires=[
        # -*- Extra requirements: -*-
        ],
    entry_points= {
        },
    )
