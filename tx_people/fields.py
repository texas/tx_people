from django.db import models

from . import utils


class ReducedDateField(models.CharField):
    def __init__(self, *args, **kwargs):
        validators = kwargs.get('validators', [])
        validators.append(utils.valid_reduced_date)
        kwargs.update({
            'max_length': kwargs.get('max_length', 10),
            'validators': validators,
        })
        return super(ReducedDateField, self).__init__(*args, **kwargs)


class OptionalManyToManyField(models.ManyToManyField):
    def __init__(self, *args, **kwargs):
        defaults = {
            'blank': True,
            'null': True,
        }
        defaults.update(**kwargs)
        return super(OptionalManyToManyField, self).__init__(*args, **defaults)
