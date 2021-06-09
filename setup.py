from setuptools import setup
from os import path
from io import open
import sys

here = path.abspath(path.dirname(__file__))

version_maj = sys.version_info[0]
version_min = sys.version_info[1]

if version_maj < 3:
    sys.exit("Need python 3 to run. You are trying to install this with python {}.{}".format(version_maj, version_min))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="thesoup",
    version="0.1",
    description="A soup of random python utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="hhttps://github.com/amartya00/thesoup",
    author="Amartya Datta Gupta",
    author_email="amartya00@gmail.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utils',
        'License :: GPLV2',
        'Programming Language :: Python :: 3.6',
    ],
    packages=["thesoup.utilityclasses", "thesoup.utilityfunctions"],
    install_requires=[],
    extras_require={
        'dev': [],
        'test': ["nose"],
    },
    project_urls={
        "Source": "hhttps://github.com/amartya00/thesoup"
    },
)