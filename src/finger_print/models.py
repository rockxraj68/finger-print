from django.db import models
from django.utils.translation import ugettext_lazy as _

class Person(models.Model):
    """
    Models for creating biometric records
    """
    name = models.CharField(_('Person Name'), max_length=255, db_index=True)
    bio_id = models.PositiveIntegerField(_('Biometric Id'))
    credentials = models.TextField(_('Credentials'), max_length=255, db_index=True)
    created_on = models.DateTimeField('Created On', auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField('Updated On', auto_now=True)

    def __str__(self):
        return self.name
