#!/usr/bin/env python
import ast
import os
import codecs
import re

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))
init = os.path.join(ROOT, 'src', '{{cookiecutter.package_name}}', '__init__.py')

_version_re = re.compile(r'__version__\s+=\s+(.*)')
_name_re = re.compile(r'NAME\s+=\s+(.*)')

with open(init, 'rb') as f:
    content = f.read().decode('utf-8')
    version = str(ast.literal_eval(_version_re.search(content).group(1)))
    name = str(ast.literal_eval(_name_re.search(content).group(1)))



def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts)).read()


tests_requires = read('src/requirements/testing.pip')
install_requires = read('src/requirements/install.pip')

setup(
    name=name,
    version=version,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    license="{{cookiecutter.open_source_license}}",
    description='{{cookiecutter.project_short_description}}',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require={
        'dev': tests_requires,
        'tests': tests_requires,
    },
    platforms=['linux'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers'
    ]
)
