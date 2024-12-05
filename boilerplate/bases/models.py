from django.db import models
from model_utils.models import TimeStampedModel


# Main Section
class Model(TimeStampedModel, models.Model):
    is_deleted = models.BooleanField("삭제 여부", default=False, blank=True, null=True)
    deleted = models.DateTimeField("삭제 시간", blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["-created"]