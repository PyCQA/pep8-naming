PEP-8 Naming Conventions
========================

Check the PEP-8 naming conventions.

This module provides a plugin for ``flint``, the Python code checker.


Installation
------------

You can install, upgrade, uninstall ``flint-naming`` with these commands::

  $ pip install flint-naming
  $ pip install --upgrade flint-naming
  $ pip uninstall flint-naming


Plugin for Flint
----------------

When both ``flint`` and ``flint-naming`` are installed, the plugin is
available in ``flint``::

  $ flint --version
  0.1 (pep8: 1.4.2, pyflakes: 0.6.1, naming: 0.1)

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

0.1 - 2013-02-11
````````````````
* First release
