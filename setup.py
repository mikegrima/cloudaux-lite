"""
cloudaux-lite
=====

Cloud Auxiliary (Lite) is a python wrapper and orchestration module for interacting with cloud providers
This is the slimmed-down fork of Netflix-Skunkworks/cloudaux without the unsupported code.

:copyright: (c) 2016 by Netflix, see AUTHORS for more
:copyright: (c) 2023 by Mike Grima, see AUTHORS for more
:license: Apache, see LICENSE for more details.
"""
import sys
import os.path

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

# When executing the setup.py, we need to be able to import ourselves.  This
# means that we need to add the src/ directory to the sys.path

sys.path.insert(0, ROOT)

about = {}
with open(os.path.join(ROOT, "cloudaux", "__about__.py")) as f:
    exec(f.read(), about)

classifiers = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
]

install_requires = [
    'boto3',
    'botocore',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'moto',
    'tox',
]

docs_require = []

dev_require = []

setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__email__"],
    url=about["__uri__"],
    description=about["__summary__"],
    long_description=open(os.path.join(ROOT, 'README.md')).read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=classifiers,
    extras_require={
        'tests': tests_require,
        'docs': docs_require,
        'dev': dev_require
    }
)
