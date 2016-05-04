"""
file        :   models.py
date        :   2016-05-03
module      :   core
classes     :   BaseModel
description :   base model for model inheritance
"""

from django.db import models

from core.util import gen_uid


class BaseModel (models.Model):

    """
    Abstract base class model that provides self-updating `created`
    and `modified` fields. It also provides slug and description fields
    that are common to all models.
    """
    uid = models.CharField(max_length=10, default=gen_uid(10))
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="create datetime")
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name="modify datetime")
    slug = models.SlugField(help_text='slug for URLs', blank=True)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True
