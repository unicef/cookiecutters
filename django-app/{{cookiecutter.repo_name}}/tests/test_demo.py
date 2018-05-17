# -*- coding: utf-8 -*-

import pytest
from demo.models import DemoModel


@pytest.mark.django_db(transaction=False)
def test_model():
    m = DemoModel()
    m.save()
    assert m.pk
