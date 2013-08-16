import random

from django.core.exceptions import ValidationError
from django.test import TestCase

from tx_people import utils


class valid_reduced_date_TestCase(TestCase):
    @property
    def random_year(self):
        return '{0}'.format(random.randint(1000, 3000))

    @property
    def random_month(self):
        return '{0:02d}'.format(random.randint(1, 12))

    @property
    def random_day(self):
        # Avoid possible issues with February dates by only going to 28
        return '{0:02d}'.format(random.randint(1, 28))

    def test_accepts_a_valid_year(self):
        self.assertEqual(None, utils.valid_reduced_date(self.random_year))

    def test_accepts_valid_year_month(self):
        date = '-'.join([self.random_year, self.random_month])
        self.assertEqual(None, utils.valid_reduced_date(date))

    def test_accepts_valid_year_month_day(self):
        date = '-'.join([self.random_year, self.random_month, self.random_day])
        self.assertEqual(None, utils.valid_reduced_date(date))

    def test_raises_on_day_month_year(self):
        invalid_date = '-'.join([self.random_day, self.random_month,
                self.random_year])
        with self.assertRaises(ValidationError):
            utils.valid_reduced_date(invalid_date)

    def test_raises_on_month_day_year(self):
        invalid_date = '-'.join([self.random_month, self.random_day,
                self.random_year])
        with self.assertRaises(ValidationError):
            utils.valid_reduced_date(invalid_date)

    def test_raised_exception_has_code_invalid_value(self):
        invalid_date = '-'.join([self.random_month, self.random_day,
                self.random_year])
        with self.assertRaises(ValidationError) as e:
            utils.valid_reduced_date(invalid_date)
        self.assertEqual('invalid_choice', e.exception.code)

    def test_raised_exception_message_explains_error(self):
        invalid_date = '-'.join([self.random_month, self.random_day,
                self.random_year])
        with self.assertRaises(ValidationError) as e:
            utils.valid_reduced_date(invalid_date)
        expected = 'Value must follow YYYY-MM-DD pattern'
        self.assertEqual(expected, e.exception.messages[0])

    def test_raises_on_feb_29_2013(self):
        invalid_date = '2013-02-29'
        with self.assertRaises(ValidationError):
            utils.valid_reduced_date(invalid_date)

    def test_passes_on_feb_29_2012(self):
        valid_date = '2012-02-29'
        self.assertEqual(None, utils.valid_reduced_date(valid_date))

    def test_raised_exceptions_on_invalid_date_different(self):
        invalid_date = '2013-02-29'
        with self.assertRaises(ValidationError) as e:
            utils.valid_reduced_date(invalid_date)
        expected = 'Value must be a valid date'
        self.assertEqual(expected, e.exception.messages[0])

    def test_raised_exception_on_invalid_date_has_code_invalid_value(self):
        invalid_date = '2013-02-29'
        with self.assertRaises(ValidationError) as e:
            utils.valid_reduced_date(invalid_date)
        self.assertEqual('invalid_choice', e.exception.code)
