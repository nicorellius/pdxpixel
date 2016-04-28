from django.db.models.signals import class_prepared
from django.db import models


def alter_flatpages(sender, **kwargs):
    if sender.__module__ == 'django.contrib.flatpages.models' and sender.__name__ == 'FlatPage':
        description = models.CharField(max_length=500)
        description.contribute_to_class(sender, 'description')

class_prepared.connect(alter_flatpages)
