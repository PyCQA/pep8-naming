.. image:: https://travis-ci.org/PyCQA/pep8-naming.svg?branch=master
    :target: https://travis-ci.org/PyCQA/pep8-naming

PEP-8 Naming Conventions
========================

Check the PEP-8 naming conventions.

This module provides a plugin for ``flake8``, the Python code checker.

(It replaces the plugin ``flint-naming`` for the ``flint`` checker.)


Installation
------------

You can install, upgrade, uninstall ``pep8-naming`` with these commands::

  $ pip install pep8-naming
  $ pip install --upgrade pep8-naming
  $ pip uninstall pep8-naming


Plugin for Flake8
-----------------

When both ``flake8`` and ``pep8-naming`` are installed, the plugin is
available in ``flake8``::

  $ flake8 --version
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
| N807 | function name should not start or end with '__'       |
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
