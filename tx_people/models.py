from django.db import models

from . import fields
from . import mixins
from .conf import settings


class OtherNames(models.Model):
    """
    Other current or previous names for an Organization or Person

    See: http://popoloproject.com/schemas/other_name.json#
    """
    name = models.CharField(max_length=250)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Identifier(models.Model):
    """
    Identifiers for an Organization or Person

    See: http://popoloproject.com/schemas/identifier.json#
    """
    identifier = models.CharField(max_length=250)
    scheme = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return u'{scheme}://{identifier}'.format(scheme=self.scheme,
                identifier=self.identifier)


class Link(models.Model):
    """
    Links for an Organization or Person

    See: http://popoloproject.com/schemas/link.json#
    """
    url = models.URLField()
    note = models.TextField()

    def __unicode__(self):
        return self.url


class Source(models.Model):
    """
    Model to keep track of source information.

    A ``Source`` can apply to one or more ``Person``, ``Post``, or
    ``Organization`` models.
    """
    link = models.URLField()

    def __unicode__(self):
        return self.link


class ContactDetail(mixins.TimeTrackingMixin, mixins.OptionalLabelMixin,
        models.Model):
    """
    Contact Details for Persons, Organizations, or Posts

    See: http://popoloproject.com/schemas/contact_detail.json
    """
    type = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    note = models.TextField(null=True, blank=True)
    sources = fields.OptionalManyToManyField(Source,
        related_name='contact_detail')


class Organization(mixins.TimeTrackingMixin,
        mixins.create_named_entities_mixin(related_name='organizations'),
        models.Model):
    """
    Represents an Organization

    See: http://popoloproject.com/schemas/organization.json
    """

    identifiers = fields.OptionalManyToManyField(Identifier,
            related_name='organizations')
    classification = models.CharField(max_length=250, null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True,
            blank=True)
    founding_date = fields.ReducedDateField(null=True, blank=True)
    dissolution_date = fields.ReducedDateField(null=True, blank=True)
    contact_details = fields.OptionalManyToManyField(ContactDetail,
            related_name='organizations')
    links = fields.OptionalManyToManyField(Link, related_name='organizations')
    sources = fields.OptionalManyToManyField(Source,
            related_name='organizations')


class Post(mixins.ReducedDateStartAndEndMixin, mixins.TimeTrackingMixin,
        mixins.OptionalLabelAndRoleMixin, models.Model):
    """
    Information about a given Post that a Person hold within an Organization

    See: http://popoloproject.com/schemas/post.json
    """
    organization = models.ForeignKey(Organization, related_name='posts')
    contact_details = fields.OptionalManyToManyField(ContactDetail,
            related_name='posts')
    links = fields.OptionalManyToManyField(Link, related_name='posts')
    sources = fields.OptionalManyToManyField(Source, related_name='posts')


class Membership(mixins.ReducedDateStartAndEndMixin, mixins.TimeTrackingMixin,
        mixins.OptionalLabelAndRoleMixin, models.Model):
    """
    Represents a Person

    See: http://popoloproject.com/schemas/membership.json
    """
    person = models.ForeignKey('Person', related_name='memberships')
    organization = models.ForeignKey(Organization, related_name='members')
    post = models.ForeignKey(Post, related_name='members', null=True,
            blank=True)
    contact_details = fields.OptionalManyToManyField(ContactDetail,
            related_name='memberships')
    links = fields.OptionalManyToManyField(Link, related_name='memberships')
    sources = fields.OptionalManyToManyField(Source, related_name='memberships')


class Person(mixins.TimeTrackingMixin,
        mixins.create_named_entities_mixin(related_name='people'),
        models.Model):
    """
    Represents a Person

    See: http://popoloproject.com/schemas/person.json
    """
    organization = models.ManyToManyField(Organization, through=Membership,
            related_name='member')
    identifiers = fields.OptionalManyToManyField(Identifier,
            related_name='people')
    family_name = fields.OptionalCharField(max_length=250)
    given_name = fields.OptionalCharField(max_length=250)
    additional_name = fields.OptionalCharField(max_length=250)
    honorific_prefix = fields.OptionalCharField(max_length=250)
    honorific_suffix = fields.OptionalCharField(max_length=250)
    patronymic_name = fields.OptionalCharField(max_length=250)
    sort_name = fields.OptionalCharField(max_length=250)
    email = fields.OptionalCharField(max_length=250)
    gender = fields.OptionalCharField(max_length=10)
    birth_date = fields.OptionalReducedDateField()
    death_date = fields.OptionalReducedDateField()
    image = models.ImageField(upload_to=settings.TX_PEOPLE_UPLOAD_TO,
            null=True, blank=True)
    summary = fields.OptionalCharField(max_length=250)
    biography = models.TextField(blank=True, null=True)
    contact_details = fields.OptionalManyToManyField(ContactDetail,
            related_name='people')
    links = fields.OptionalManyToManyField(Link, related_name='people')
    sources = fields.OptionalManyToManyField(Source, related_name='people')
