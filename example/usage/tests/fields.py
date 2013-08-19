import random

from django.core.exceptions import ValidationError
from django.db.models import CharField, ManyToManyField
from django.test import TestCase

from tx_people import fields
from tx_people import models
from tx_people import utils

from ._utils import RandomDatesMixin


class ReducedDateFieldTestCase(RandomDatesMixin, TestCase):
    def test_defaults_to_max_length_of_ten(self):
        field = fields.ReducedDateField()
        self.assertEqual(10, field.max_length)

    def test_custom_max_length_can_be_used(self):
        random_max_length = random.randint(11, 20)
        field = fields.ReducedDateField(max_length=random_max_length)
        self.assertEqual(random_max_length, field.max_length)

    def test_includes_valid_reduced_date_validator(self):
        field = fields.ReducedDateField()
        self.assert_(utils.valid_reduced_date in field.validators)

    def test_validates_valid_dates(self):
        field = fields.ReducedDateField()
        valid_dates = [
            '-'.join([self.random_year, self.random_month, self.random_day]),
            '-'.join([self.random_year, self.random_month]),
            self.random_year,
            '2012-02-29',  # leap year
        ]

        for date in valid_dates:
            field.run_validators(date)

    def test_raises_on_invalid_dates(self):
        field = fields.ReducedDateField()
        invalid_dates = [
            '-'.join([self.random_day, self.random_month, self.random_year]),
            '-'.join([self.random_month, self.random_year]),
            '2013-02-29',  # not a leap year
        ]
        for invalid_date in invalid_dates:
            with self.assertRaises(ValidationError):
                field.run_validators(invalid_date)

    def test_valid_reduced_date_added_to_existing_validators(self):
        field = fields.ReducedDateField(validators=[self, ])
        self.assert_(self in field.validators)
        self.assert_(utils.valid_reduced_date in field.validators)


class OptionalCharField(TestCase):
    def generate_random_field(self, **kwargs):
        r = random.randint(10, 250)
        return fields.OptionalCharField(max_length=r, **kwargs)

    def setUp(self):
        self.field = self.generate_random_field()

    def test_is_a_charfield_subclass(self):
        self.assert_(CharField in self.field.__class__.__mro__)

    def test_null_defaults_to_true(self):
        self.assertTrue(self.field.null)
        self.assertFalse(self.generate_random_field(null=False).null)

    def test_blank_defaults_to_true(self):
        self.assertTrue(self.field.blank)
        self.assertFalse(self.generate_random_field(blank=False).blank)


class OptionalManyToManyField(TestCase):
    def generate_random_field(self, **kwargs):
        return fields.OptionalManyToManyField(models.Person, **kwargs)

    def setUp(self):
        self.field = self.generate_random_field()

    def test_is_a_many_to_many_subclass(self):
        self.assert_(ManyToManyField in self.field.__class__.__mro__)

    def test_null_defaults_to_true(self):
        self.assertTrue(self.field.null)
        self.assertFalse(self.generate_random_field(null=False).null)

    def test_blank_defaults_to_true(self):
        self.assertTrue(self.field.blank)
        self.assertFalse(self.generate_random_field(blank=False).blank)
