from django.db import models

from . import fields


class ReducedDateStartAndEndMixin(models.Model):
    """
    Provides a ``start_date`` and ``end_date`` field for a given model

    This is a common set of fields found throughout Popolo models.
    """
    class Meta:
        abstract = True

    start_date = fields.ReducedDateField()
    end_date = fields.ReducedDateField()


class TimeTrackingMixin(models.Model):
    """
    Mixin for adding a ``created_at`` and ``updated_at`` field

    Most entities inside Popolo provide an auto-generated ``created_at``
    and ``updated_at`` time stamp.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
