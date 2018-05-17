# -*- coding: utf-8 -*-

import logging
from django.db import models

logger = logging.getLogger(__name__)


class DemoModel(models.Model):
    class Meta:
        ordering = ("id",)
