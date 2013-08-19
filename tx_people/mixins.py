from django.db import models

from . import fields


class ReducedDateStartAndEndMixin(models.Model):
    class Meta:
        abstract = True

    start_date = fields.ReducedDateField()
    end_date = fields.ReducedDateField()


class TimeTrackingMixin(models.Model):
    """
    Mixin for adding a created_at and updated_at field
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
