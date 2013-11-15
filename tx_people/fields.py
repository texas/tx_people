from django.db import models

from . import utils


class ReducedDateField(models.CharField):
    """
    Provides a means of storing an `ISO-8601:2004`_ reduced date

    This is meant to be a fuzzy date, allowing for the following types
    of dates to be stored:

    * YYYY
    * YYYY-MM
    * YYYY-MM-DD

    This relies on the ``utils.valid_reduced_date`` validator to ensure
    that the date follows the correct pattern and is a valid date.

    .. _ISO-8601:2004: https://github.com/opennorth/popolo-spec/wiki/ISO-8601%3A2004-formats
    """
    def __init__(self, *args, **kwargs):
        validators = kwargs.get('validators', [])
        validators.append(utils.valid_reduced_date)
        kwargs.update({
            'max_length': kwargs.get('max_length', 10),
            'validators': validators,
        })
        return super(ReducedDateField, self).__init__(*args, **kwargs)


class OptionalReducedDateField(ReducedDateField):
    """
    Same as ``ReducedDateField``, except it is not required
    """
    def __init__(self, *args, **kwargs):
        defaults = {
            'blank': True,
            'null': True,
        }
        defaults.update(**kwargs)
        return super(OptionalReducedDateField, self).__init__(*args, **defaults)


class OptionalCharField(models.CharField):
    """Same as Django's built-in ``CharField``, except optional"""
    def __init__(self, *args, **kwargs):
        defaults = {
            'blank': True,
            'null': True,
        }
        defaults.update(**kwargs)
        return super(OptionalCharField, self).__init__(*args, **defaults)


class OptionalManyToManyField(models.ManyToManyField):
    """Same as Django's built-in ``ManyToManyField``, except optional"""
    def __init__(self, *args, **kwargs):
        defaults = {
            'blank': True,
            'null': True,
        }
        defaults.update(**kwargs)
        return super(OptionalManyToManyField, self).__init__(*args, **defaults)


# Provide South with the information required to process custom fields.
#
# This fails quietly if there is an ``ImportError`` as it none of this
# matters if South isn't installed.
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^tx_people\.fields\..*Field"])
except ImportError:
    pass
