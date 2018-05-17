# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, register

from .models import DemoModel


@register(DemoModel)
class DemoAdmin(ModelAdmin):
    pass
