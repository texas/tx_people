from django.db import models

# TODO: Find a better location for this
from . import fields


class Organization(models.Model):
    """
    Represents an Organization
    """

    id = models.CharField(max_length=250, primary_key=True)
    name = models.CharField(max_length=250)
    classification = models.CharField(max_length=250, null=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', null=True,
            blank=True)
    founding_date = fields.ReducedDateField(null=True, blank=True)
    dissolution_date = fields.ReducedDateField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


class OrganizationSource(models.Model):
    """
    # TODO
    """
    link = models.URLField()
    organization = models.ForeignKey(Organization, related_name='sources')


class Post(models.Model):
    organization = models.ForeignKey(Organization, related_name='posts')


class Membership(models.Model):
    organization = models.ForeignKey(Organization, related_name='members')
    member = models.ForeignKey('Person', related_name='memberships')
    post = models.ForeignKey(Post, related_name='members', null=True,
            blank=True)


class Person(models.Model):
    organization = models.ManyToManyField(Organization, through=Membership,
            related_name='member')


class ContactDetail(models.Model):
    """
    Contact Details for Persons or Organizations

    See: http://popoloproject.com/schemas/contact_detail.json
    """

    person = models.ForeignKey(Person, related_name='contact_details')
    label = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactDetailSources(models.Model):
    link = models.URLField()
    contact_detail = models.ForeignKey(ContactDetail, related_name='sources')


class OtherNames(models.Model):
    """
    Other current or previous names for an Organization or Person

    See: http://popoloproject.com/schemas/other_name.json#
    """
    name = models.CharField(max_length=250)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    # TODO: allow relationship to an Organization or Person


class Identifier(models.Model):
    """
    Identifiers for an Organization or Person

    See: http://popoloproject.com/schemas/identifier.json#
    """
    identifier = models.CharField(max_length=250)
    scheme = models.CharField(max_length=250, null=True, blank=True)

    # TODO: allow relationship to an Organization or Person


class Link(models.Model):
    """
    Links for an Organization or Person

    See: http://popoloproject.com/schemas/link.json#
    """
    url = models.URLField()
    note = models.TextField()

    # TODO: allow relationship to an Organization or Person


class Source(models.Model):
    """
    Model to keep track of source information.

    A ``Source`` can apply to one or more ``Person``, ``Post``, or
    ``Organization`` models.
    """
    link = models.URLField()
    people = fields.SourceRelationship(Person)
    posts = fields.SourceRelationship(Post)
    organizations = fields.SourceRelationship(Organization)
