import datetime
import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


VALID_REDUCED_DATE_PATTERN = r'^[0-9]{4}((-[01][0-9])?(-[0-3][0-9])?)$'
VALID_REDUCED_DATE_RE = re.compile(VALID_REDUCED_DATE_PATTERN)


valid_reduced_date = RegexValidator(regex=VALID_REDUCED_DATE_RE,
        message='Value must follow YYYY-MM-DD pattern', code='invalid_choice')
