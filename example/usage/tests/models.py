from django.test import TestCase

from tx_people import factories


class EmailTestCase(TestCase):
    def test_can_relate_to_a_person(self):
        person = factories.PersonFactory.build()
        email = factories.EmailFactory.build(person=person)

        self.assertEqual(person.pk, email.person.pk)

    def test_can_only_have_a_person_or_organization(self):
        pass
