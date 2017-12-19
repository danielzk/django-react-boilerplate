from django.db import models
from django.db.models import DateTimeField
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class ValidationModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class BaseModel(TimeStampedModel, ValidationModel):
    class Meta:
        abstract = True
