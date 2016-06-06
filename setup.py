#!/usr/bin/env python

from setuptools import setup, find_packages

PROJECT = 'qingcloudclient'
VERSION = '1.0'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='CLI for QingCloud API',
    long_description=long_description,

    author='hebin',
    author_email='491309649@qq.com',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Intended Audience :: End User',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'qingcloudclient = qingcloudclient.main:main'
        ],
        'qingcloudclient.instance': [
            'run-instances = qingcloudclient.cli.run_instances:RunInstances',
            'describe-instances = qingcloudclient.cli.describe_instances:'
            'DescribeInstances',
            'terminate-instances = qingcloudclient.cli.terminate_instances:'
            'TerminateInstances',
        ],
    },

    zip_safe=False,
)
