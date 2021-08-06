Changes
=======

0.12.1 - 2021-08-06
-------------------

* Fix potential stack exhaustion in the N818 check.

0.12.0 - 2021-07-06
-------------------

* flake8 3.9.1 or later is now required.

* N818 checks exception class names for an "Error" suffix (disabled by default).

* ``asyncSetUp`` and ``asyncTearDown`` are now exempted by default.


0.11.1 - 2020-06-16
-------------------

* Fix an AST-related AttributeError when processing decorator lists.


0.11.0 - 2020-06-16
-------------------

* ``__class_getitem__`` is now recognized as a class method.

* Support ``ast.Call`` nodes in decorator lists (``@decorator(arg)``).

* As a performance improvement, only checks for selected error codes are run.

0.10.0 - 2020-03-20
-------------------

* ``--ignore-names`` now supports globbing and applies to the N804 and N805
  checks.

* "acronym" imports are now treated as their own error code (N817).

* Metaclass detection has been improved.

* Annotated variable declarations (PEP 526) and ``:=`` variable assignments
  are now supported.

0.9.1 - 2019-11-14
------------------

* Fix line number offsets when reporting errors involving functions with
  decorators in Python 3.8 and later.

0.9.0 - 2019-11-06
------------------

* Drop support for Python 3.3 and 3.4.

* Support positional-only arguments in Python 3.8.

* Recognize ``abc.ABCMeta`` as a metaclass base type.

* ``ignore-names`` now also applies to the N803 check.

* Handle assigning exceptions to object attributes in Python 2.

0.8.2 - 2019-02-04
------------------

* Fix a problem with ``ignore-names`` option initialization.

0.8.1 - 2019-02-04
------------------

* ``ignore-names`` now also applies to the N806, N815, and N816 checks.

* ``failureException``, ``longMessage``, and ``maxDiff`` have been added to
  the default ``ignore-names`` list.

* Allow lowercase names to be imported as just ``_``.

* Allow function arguments to be named just ``_``.

* Support Python 2's tuple syntax in ``except`` clauses.

0.8.0 - 2019-01-28
------------------

* Detect N806 errors within ``for`` loops and exception handlers.

* Improve support for non-ASCII characters.

* Detect mixedCased variable names at class (N815) and global (N816) scope.

* Ignore Django's ``setUpTestData`` method by default.

* Fix column offsets for N803, N804, and N805 under Python 3.

* Detect underscores within class names as N801 errors.

* Don't flag ``__getattr__`` and ``__dir__`` as N807 errors. (See
  `PEP 562 <https://www.python.org/dev/peps/pep-0562/>`_).

* ``async`` function and method names are now checked.

* Detect N806 errors in generator expressions and comprehensions.

* Detect N81x errors in ``import x as y`` statements.

0.7.0 - 2018-05-17
------------------

* Detect N806 in ``with ... as ...:`` statements.

* Detect N806 in multiple assignment statements, e.g., ``Foo, Bar =
  unpacking``.

* Allow class names to be properly ignored.

* Remove spurious 'xxx' from error message

* Detect N807 within conditional statements.


0.6.1 - 2018-05-06
------------------

* Fix N804 check for ``cls`` used in metaclass methods (See also
  https://github.com/PyCQA/pep8-naming/issues/53)


0.6.0 - 2018-05-04
------------------

* Separate check for ``__`` in function names to its own code: N807

* Consider all metaclass methods to be class methods


0.5.0 - 2018-01-02
------------------

* Add configurable list of classmethod and staticmethod decorators

* Print the offending name as part of the error message

* Correct N804/N805 for __init_subclass__


0.4.1 - 2016-06-26
------------------

* Note to self: Never do releases before ~0600 or coffee on a Sunday.

* Fix option parsing for Flake8 3.0 (store parsed value on class)


0.4.0 - 2016-06-26
------------------

* Fix integration with Flake8 3.0.0b1

* Start testing against Python 3.5


0.3.3 - 2015-06-30
------------------

* Fix bug where ignored names were not properly split into a list.


0.3.2 - 2015-06-14
------------------

* Fix bug trying to call ``split`` on a list.


0.3.1 - 2015-06-14
------------------

* Fix optparse exception resulting from trying to register an option twice.


0.3.0 - 2015-06-14
------------------

* Relaxed N806 checking for use with namedtuples

* Add ``--ignore-names`` which allows the user to specify a list of names to
  ignore. By default this includes ``setUp``, ``tearDown``, ``setUpClass``,
  and ``tearDownClass``.


0.2.2 - 2014-04-19
------------------

* Do not require ``setuptools`` in setup.py.  It works around an issue
  with ``pip`` and Python 3.

* ``__new__`` is now considered as ``classmethod`` implicitly

* Run unit tests on travis-ci.org for python2.6, 2.7, 3.2, and 3.3

* Add unit tests and support running them with setup.py

* Support Python 3.4 


0.2.1 - 2013-02-22
------------------
* Do not require ``flake8``


0.2 - 2013-02-22
----------------

* Rename project ``flint-naming`` to ``pep8-naming``

* Fix a crash when function argument is a tuple of tuples


0.1 - 2013-02-11
----------------

* First release
