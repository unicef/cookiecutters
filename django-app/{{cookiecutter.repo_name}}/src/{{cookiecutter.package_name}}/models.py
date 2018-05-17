# -*- coding: utf-8 -*-

import logging

from django.db import models
from django.utils.translation import gettext as _

logger = logging.getLogger(__name__)


{% if cookiecutter.model_name %}class {{cookiecutter.model_name}}(models.Model):
    class Meta:
        ordering = ("id",)
        verbose_name = _("{{cookiecutter.model_name}}"){% endif %}
