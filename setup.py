import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

PACKAGE_NAME = 'bhsum'
VERSION = "1.1"
DESCRIPTION = "returns sum"
KEYWORDS = "addition"
URL = 'https://github.com/bmummareddy/bhsum'
AUTHOR = 'Bhargavi'
LICENSE = 'Eg'
REQUIRES_PYTHON = '>=3.7.0'
EXTRAS = {}

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=KEYWORDS,
    license=LICENSE,
    author=AUTHOR,
    url=URL,
    packages=find_packages(include=f"{PACKAGE_NAME}.*"),
    extras_require=EXTRAS,
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Addition: Example package",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

