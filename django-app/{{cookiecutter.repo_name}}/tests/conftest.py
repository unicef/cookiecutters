import os
import sys

import pytest


def pytest_configure(config):
    here = os.path.realpath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.join(here, 'demoproject'))


@pytest.fixture
def demomodel():
    from demo.factories import DemoModelFactory
    return DemoModelFactory()


{% if cookiecutter.model_name %}@pytest.fixture
def {{cookiecutter.model_name|lower}}():
    from {{cookiecutter.package_name}}.utils.factories import {{cookiecutter.model_name}}Factory
    return {{cookiecutter.model_name}}Factory(){% endif %}
