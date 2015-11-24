
from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = None
with open('module/version.py') as f:
    exec(f.read())
REQUIRES = []
setup(
    name = "module",
    version = __version__,
    description = "Module module",
    author = "michele.pagot",
    author_email = "michele.pagot@hotmail.it",
    url = "https://github.com/michelepagot/travistest/",
    keywords = ["module","pizza"],
    install_requires = REQUIRES,
    # bdist conditional requirements support
    extras_require={
        ':python_version=="3.2"': ['pysocks'],
        ':python_version=="3.3"': ['pysocks'],
        ':python_version=="3.4"': ['pysocks'],
        ':python_version=="3.5"': ['pysocks'],
    },
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python Module Example
    ----------------------------
    DESCRIPTION
    The Module is a module example """ )