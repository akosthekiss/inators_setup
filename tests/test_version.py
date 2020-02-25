# Copyright (c) 2020 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import datetime
import pytest

from setuptools_scm import Configuration, format_version, meta

from inators_setup.version import get_local_distance_node_date, tag_version


todaystr = datetime.date.today().strftime('%Y%m%d')

@pytest.mark.parametrize('tag, distance, node, dirty, public_version, local_version', [
    (
        '16.10', None, 'gc963e00', False,
        '16.10', ''
    ),
    (
        '17.7', 28, 'g599cc24', False,
        '17.7', '+28.g599cc24'
    ),
    (
        '16.12', None, 'g72aa042', True,
        '16.12', '+0.g72aa042.d'+todaystr
    ),
    (
        '19.3', 13, 'g800a709', True,
        '19.3', '+13.g800a709.d'+todaystr
    ),
])
def test_tag_distance_node_date(tag, distance, node, dirty, public_version, local_version):
    scm_version = meta(tag, distance=distance, node=node, dirty=dirty, config=Configuration())

    # test API
    assert tag_version(scm_version) == public_version
    assert get_local_distance_node_date(scm_version) == local_version

    # test entry points
    assert format_version(scm_version, version_scheme='inators-tag', local_scheme='inators-distance-node-date') == public_version + local_version
