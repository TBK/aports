"""
Zeyple automatically encrypts outgoing emails with GPG.

See:
https://infertux.com/labs/zeyple/
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name = "zeyple",
      version = "1.2.1",
      author = "Cédric Félizard",
      author_email = "cedric@felizard.fr",
      url = "https://github.com/infertux/zeyple",
      description = "Zeyple automatically encrypts outgoing emails with GPG.",
      scripts = ["zeyple"],
      # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: SMTP',
        'Topic :: Utilities'
      ]
)
