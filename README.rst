PEP-8 Naming Conventions
========================

Check the PEP-8 naming conventions.

This module provides a plugin for ``flake8``, the Python code checker.


Installation
------------

You can install, upgrade, uninstall ``pep8-naming`` with these commands::

  $ pip install pep8-naming
  $ pip install --upgrade pep8-naming
  $ pip uninstall pep8-naming


Plugin for Fake8
----------------

.. warning::
   This feature requires ``flake8`` version 2.0 which is not released at this time.

When both ``flake8`` and ``pep8-naming`` are installed, the plugin is
available in ``flake8``::

  $ fake8 --version
  2.0 (pep8: 1.4.3, pyflakes: 0.6.1, naming: 0.2)

By default the plugin is enabled.

These error codes are emitted:

+------+-------------------------------------------------------+
| code | sample message                                        |
+======+=======================================================+
| N801 | class names should use CapWords convention            |
+------+-------------------------------------------------------+
| N802 | function name should be lowercase                     |
+------+-------------------------------------------------------+
| N803 | argument name should be lowercase                     |
+------+-------------------------------------------------------+
| N804 | first argument of a classmethod should be named 'cls' |
+------+-------------------------------------------------------+
| N805 | first argument of a method should be named 'self'     |
+------+-------------------------------------------------------+
| N806 | variable in function should be lowercase              |
+------+-------------------------------------------------------+
+------+-------------------------------------------------------+
| N811 | constant imported as non constant                     |
+------+-------------------------------------------------------+
| N812 | lowercase imported as non lowercase                   |
+------+-------------------------------------------------------+
| N813 | camelcase imported as lowercase                       |
+------+-------------------------------------------------------+
| N814 | camelcase imported as constant                        |
+------+-------------------------------------------------------+


Changes
-------

0.2 - unreleased
````````````````
* Rename project ``flint-naming`` to ``pep8-naming``

* Fix a crash when function argument is a tuple of tuples.


0.1 - 2013-02-11
````````````````
* First release
