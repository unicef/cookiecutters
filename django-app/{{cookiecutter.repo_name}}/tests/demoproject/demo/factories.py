# -*- coding: utf-8 -*-

from factory import DjangoModelFactory


class DemoModelFactory(DjangoModelFactory):
    class Meta:
        model = 'demo.DemoModel'
        django_get_or_create = ('id',)
