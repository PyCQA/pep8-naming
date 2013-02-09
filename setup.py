# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup


def get_version(fname='flint_naming.py'):
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


setup(
    name='flint-naming',
    version=get_version(),
    description="Check PEP-8 naming conventions, plugin for flint",
    long_description=get_long_description(),
    keywords='flint pep8',
    author='Florent Xicluna',
    author_email='florent.xicluna@gmail.com',
    url='https://github.com/florentx/flint_naming',
    license='Expat license',
    py_modules=['flint_naming'],
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'flint.extension': [
            'N80 = flint_naming:NamingChecker',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
