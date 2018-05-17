# -*- coding: utf-8

from django.apps import AppConfig


class Config(AppConfig):
    name = '{{ cookiecutter.package_name }}'
    label = '{{ cookiecutter.package_name }}'
