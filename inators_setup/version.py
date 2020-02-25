# Copyright (c) 2020 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.


def tag_version(version):
    return version.format_with('{tag}')


def get_local_distance_node_date(version):
    if version.exact and not version.dirty:
        return ''
    parts = ['{distance}'.format(distance=version.distance)]
    if version.node:
        parts.append('{node}'.format(node=version.node))
    if version.dirty:
        parts.append('d{time:%Y%m%d}'.format(time=version.time))
    return '+{parts}'.format(parts='.'.join(parts))
