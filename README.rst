PEP-8 Naming Conventions
========================

.. image:: https://badge.fury.io/py/pep8-naming.png
    :target: http://badge.fury.io/py/pep8-naming
    
.. image:: https://travis-ci.org/flintwork/pep8-naming.png?branch=master
        :target: https://travis-ci.org/flintwork/pep8-naming

.. image:: https://pypip.in/d/pep8-naming/badge.png
        :target: https://crate.io/packages/pep8-naming?version=latest

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

0.3.1 - 2015-06-14
``````````````````

* Fix optparse exception resulting from trying to register an option twice.


0.3.0 - 2015-06-14
``````````````````

* Relaxed N806 checking for use with namedtuples

* Add ``--ignore-names`` which allows the user to specify a list of names to
  ignore. By default this includes ``setUp``, ``tearDown``, ``setUpClass``,
  and ``tearDownClass``.


0.2.2 - 2014-04-19
``````````````````
* Do not require ``setuptools`` in setup.py.  It works around an issue
  with ``pip`` and Python 3.

* ``__new__`` is now considered as ``classmethod`` implicitly

* Run unit tests on travis-ci.org for python2.6, 2.7, 3.2, and 3.3

* Add unit tests and support running them with setup.py

* Support Python 3.4 


0.2.1 - 2013-02-22
``````````````````
* Do not require ``flake8``


0.2 - 2013-02-22
````````````````
* Rename project ``flint-naming`` to ``pep8-naming``

* Fix a crash when function argument is a tuple of tuples


0.1 - 2013-02-11
````````````````
* First release
