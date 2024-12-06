from django.db import models
from django.db.models import Manager
from django.utils import timezone
from model_utils.models import TimeStampedModel

from boilerplate.bases.managers import AvailableManager


# Main Section
class Model(TimeStampedModel, models.Model):
    is_deleted = models.BooleanField("삭제 여부", default=False, blank=True, null=True)
    deleted = models.DateTimeField("삭제 시간", blank=True, null=True)

    objects = Manager()
    available = AvailableManager()

    class Meta:
        abstract = True
        ordering = ["-created"]

    def soft_delete(self):
        self.is_deleted = True
        self.deleted = timezone.now()
        self.save(update_fields=["is_deleted", "deleted"])
