# Copyright (c) 2020 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

from setuptools import find_packages, setup


setup(
    name='inators_setup',
    packages=find_packages(),
    url='https://github.com/renatahodovan/inators_setup',
    license='BSD',
    author='Renata Hodovan, Akos Kiss',
    author_email='hodovan@inf.u-szeged.hu, akiss@inf.u-szeged.hu',
    description='inators_setup: package setup utilities for inators',
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'setuptools_scm.version_scheme': [
            'inators-tag = inators_setup.version:tag_version',
        ],
        'setuptools_scm.local_scheme': [
            'inators-distance-node-date = inators_setup.version:get_local_distance_node_date',
        ],
    }
)
