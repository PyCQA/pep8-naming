# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup
from setuptools.command.test import test as TestCommand


def get_version(fname='src/pep8ext_naming.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


class RunTests(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import run_tests
        import sys
        errno = run_tests.main()
        sys.exit(errno)


setup(
    name='pep8-naming',
    version=get_version(),
    description="Check PEP-8 naming conventions, plugin for flake8",
    long_description=get_long_description(),
    keywords='flake8 pep8 naming',
    author='Florent Xicluna',
    author_email='florent.xicluna@gmail.com',
    url='https://github.com/PyCQA/pep8-naming',
    license='Expat license',
    package_dir={'': 'src'},
    py_modules=['pep8ext_naming'],
    install_requires=['flake8>=3.9.1', 'flake8_polyfill>=1.0.2,<2'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'N8 = pep8ext_naming:NamingChecker',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    cmdclass={'test': RunTests},
)
