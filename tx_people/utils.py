import datetime
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


VALID_REDUCED_DATE_PATTERN = r'^[0-9]{4}((-[01][0-9])?(-[0-3][0-9])?)$'
VALID_REDUCED_DATE_RE = re.compile(VALID_REDUCED_DATE_PATTERN)


class ReducedDateValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        kwargs.update({
            'regex': VALID_REDUCED_DATE_RE,
            'message': 'Value must follow YYYY-MM-DD pattern',
            'code': 'invalid_choice',
        })
        return super(ReducedDateValidator, self).__init__(*args, **kwargs)

    def __call__(self, value):
        super(ReducedDateValidator, self).__call__(value)
        for format in ['%Y-%m-%d', '%Y-%m', '%Y']:
            try:
                datetime.datetime.strptime(value, format)
                return
            except ValueError:
                pass
        raise ValidationError('Value must be a valid date',
                code='invalid_choice')


valid_reduced_date = ReducedDateValidator()
