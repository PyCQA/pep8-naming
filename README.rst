PEP 8 Naming Conventions
========================

Check your code against `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_
naming conventions.

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

Error Codes
-----------

These error codes are emitted:

+---------+-----------------------------------------------------------------+
| code    | sample message                                                  |
+=========+=================================================================+
| _`N801` | class names should use CapWords convention (`class names`_)     |
+---------+-----------------------------------------------------------------+
| _`N802` | function name should be lowercase (`function names`_)           |
+---------+-----------------------------------------------------------------+
| _`N803` | argument name should be lowercase (`function arguments`_)       |
+---------+-----------------------------------------------------------------+
| _`N804` | first argument of a classmethod should be named 'cls'           |
|         | (`function arguments`_)                                         |
+---------+-----------------------------------------------------------------+
| _`N805` | first argument of a method should be named 'self'               |
|         | (`function arguments`_)                                         |
+---------+-----------------------------------------------------------------+
| _`N806` | variable in function should be lowercase                        |
+---------+-----------------------------------------------------------------+
| _`N807` | function name should not start and end with '__'                |
+---------+-----------------------------------------------------------------+
| _`N811` | constant imported as non constant (`constants`_)                |
+---------+-----------------------------------------------------------------+
| _`N812` | lowercase imported as non-lowercase                             |
+---------+-----------------------------------------------------------------+
| _`N813` | camelcase imported as lowercase                                 |
+---------+-----------------------------------------------------------------+
| _`N814` | camelcase imported as constant                                  |
|         | (distinct from `N817`_ for selective enforcement)               |
+---------+-----------------------------------------------------------------+
| _`N815` | mixedCase variable in class scope                               |
|         | (`constants`_, `method names`_)                                 |
+---------+-----------------------------------------------------------------+
| _`N816` | mixedCase variable in global scope (`constants`_)               |
+---------+-----------------------------------------------------------------+
| _`N817` | camelcase imported as acronym                                   |
|         | (distinct from `N814`_ for selective enforcement)               |
+---------+-----------------------------------------------------------------+
| _`N818` | error suffix in exception names (`exceptions`_)                 |
+---------+-----------------------------------------------------------------+

.. _class names: https://www.python.org/dev/peps/pep-0008/#class-names
.. _constants: https://www.python.org/dev/peps/pep-0008/#constants
.. _exceptions: https://www.python.org/dev/peps/pep-0008/#exception-names
.. _function names: https://www.python.org/dev/peps/pep-0008/#function-and-variable-names
.. _function arguments: https://www.python.org/dev/peps/pep-0008/#function-and-method-arguments
.. _method names: https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables

Options
-------

The following flake8 options are added:

--ignore-names              Ignore errors for specific names or glob patterns.

                            Currently, this option can only be used for N802, N803, N804, N805, N806, N815, and N816 errors.

                            Default: ``setUp,tearDown,setUpClass,tearDownClass,asyncSetUp,asyncTearDown,setUpTestData,failureException,longMessage,maxDiff``.

--classmethod-decorators    List of method decorators pep8-naming plugin should consider class method.

                            Used to prevent false N804 errors.

                            Default: ``classmethod``.

--staticmethod-decorators   List of method decorators pep8-naming plugin should consider static method.

                            Used to prevent false N805 errors.

                            Default: ``staticmethod``.
