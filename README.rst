=============
inators_setup
=============

``inators_setup`` is a collection of utilities useful for the setup of packages.
It is mostly used by the *...inator* project family, whence its name.


``setuptools_scm`` plugin
=========================

One (and currently, the only one) functionality of ``inators_setup`` is being
a `setuptools_scm`_ plugin. It adds the public version scheme **inators-tag**
and the local version scheme **inators-distance-node-date** to those already
provided by ``setuptools_scm``. When used together, these scheme implementations
work well with dated-based versioning (or in any other versioning where the next
development version cannot be guessed as in semver).

.. _`setuptools_scm`: https://github.com/pypa/setuptools_scm

The scheme implementations render the version roughly as follows:

- exactly on a version tag:
  ``{tag}``
- a number of revisions after a version tag:
  ``{tag}+{distance}.{scm letter}{revision hash}``
- uncommitted changes in the working directory (even if on a version tag):
  ``{tag}+{distance}.{scm letter}{revision hash}.dYYYYMMDD``

To use this versioning, add ``inators_setup`` to ``setup_requires`` in
``setup.py``, and also specify the ``inators-*`` schemes in ``use_scm_version``:

.. code-block:: python

    from setuptools import setup
    setup(
        # ...,
        use_scm_version={
            'version_scheme': 'inators-tag',
            'local_scheme': 'inators-distance-node-date',
        },
        setup_requires=['setuptools_scm', 'inators_setup'],
        # ...,
    )


Copyright and Licensing
=======================

Licensed under the BSD 3-Clause License_.

.. _License: LICENSE.rst
