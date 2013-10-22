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


class OptionalLabelMixin(models.Model):
    """
    Provides an optional ``label`` field and default ``__unicode__``

    """

    class Meta:
        abstract = True

    label = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.label


class OptionalLabelAndRoleMixin(OptionalLabelMixin, models.Model):
    """
    Provides an optional ``label`` and ``role`` field

    This is shared by both ``Post`` and ``Membership``.
    """

    class Meta:
        abstract = True

    role = models.CharField(max_length=250, null=True, blank=True)


def create_named_entities_mixin(related_name):
    class NameMixin(models.Model):
        """
        Provides a ``name`` and ``other_name`` field and __unicode__ method

        This is shared by both ``Organization`` and ``Person``, both of
        which have a ``name`` and ``other_name``.  The ``related_name`
        argument is used to set up the reversed name.
        """

        class Meta:
            abstract = True

        name = models.CharField(max_length=250)
        other_name = fields.OptionalManyToManyField('OtherNames',
                related_name=related_name)

        def __unicode__(self):
            return self.name

    return NameMixin
