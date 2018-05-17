# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin, register

{% if cookiecutter.model_name %}from .models import {{cookiecutter.model_name}}


@register({{cookiecutter.model_name}})
class {{cookiecutter.model_name}}Admin(ModelAdmin):
    pass{% endif %}
