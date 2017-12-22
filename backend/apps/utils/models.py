from django.db import models
from django.db.models import DateTimeField
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from polymorphic import models as polymorphic_models


class ValidationModelMixin(object):
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class TimeStampedSaveModelMixin(object):
    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = now()
        super().save(*args, **kwargs)


class TimeStampedModel(TimeStampedSaveModelMixin, models.Model):
    created_at = DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = DateTimeField(_('Updated at'), null=True, editable=False)

    class Meta:
        abstract = True


class BaseModel(ValidationModelMixin, TimeStampedModel):
    class Meta:
        abstract = True


class TimeStampedPolymorphicModel(TimeStampedSaveModelMixin,
                                  polymorphic_models.PolymorphicModel):
    created_at = DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = DateTimeField(_('Updated at'), null=True, editable=False)

    class Meta:
        abstract = True


class BasePolymorphicModel(ValidationModelMixin, TimeStampedPolymorphicModel):
    class Meta:
        abstract = True
