import uuid

from django.db import models
from django.db.models import CharField, DateTimeField
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


class CodenameModel(models.Model):
    codename = CharField(max_length=36, default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True


class TimeStampedModel(TimeStampedSaveModelMixin, models.Model):
    created_at = DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = DateTimeField(_('Updated at'), null=True, editable=False)

    class Meta:
        abstract = True


class BaseModel(ValidationModelMixin, CodenameModel, TimeStampedModel):
    class Meta:
        abstract = True


class CodenamePolymorphicModel(polymorphic_models.PolymorphicModel):
    codename = CharField(max_length=36, default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True


class TimeStampedPolymorphicModel(TimeStampedSaveModelMixin,
                                  polymorphic_models.PolymorphicModel):
    created_at = DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = DateTimeField(_('Updated at'), null=True, editable=False)

    class Meta:
        abstract = True


class BasePolymorphicModel(ValidationModelMixin,
                           CodenamePolymorphicModel,
                           TimeStampedPolymorphicModel):
    class Meta:
        abstract = True
