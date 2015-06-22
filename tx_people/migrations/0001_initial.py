# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tx_people.fields
import tx_people.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(max_length=250, null=True, blank=True)),
                ('type', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250)),
                ('note', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=250)),
                ('scheme', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('end_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(max_length=250, null=True, blank=True)),
                ('role', models.CharField(max_length=250, null=True, blank=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(related_name='memberships', to='tx_people.ContactDetail', blank=True)),
                ('links', tx_people.fields.OptionalManyToManyField(related_name='memberships', to='tx_people.Link', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('classification', models.CharField(max_length=250, null=True, blank=True)),
                ('founding_date', tx_people.fields.ReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('dissolution_date', tx_people.fields.ReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('contact_details', tx_people.fields.OptionalManyToManyField(related_name='organizations', to='tx_people.ContactDetail', blank=True)),
                ('identifiers', tx_people.fields.OptionalManyToManyField(related_name='organizations', to='tx_people.Identifier', blank=True)),
                ('links', tx_people.fields.OptionalManyToManyField(related_name='organizations', to='tx_people.Link', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherNames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('note', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('family_name', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('given_name', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('additional_name', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('honorific_prefix', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('honorific_suffix', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('patronymic_name', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('sort_name', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('email', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('gender', tx_people.fields.OptionalCharField(max_length=10, null=True, blank=True)),
                ('birth_date', tx_people.fields.OptionalReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('death_date', tx_people.fields.OptionalReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('image', models.ImageField(null=True, upload_to=b'tx_people/', blank=True)),
                ('summary', tx_people.fields.OptionalCharField(max_length=250, null=True, blank=True)),
                ('biography', models.TextField(null=True, blank=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.ContactDetail', blank=True)),
                ('ethnicities', tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.Ethnicity', blank=True)),
                ('identifiers', tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.Identifier', blank=True)),
                ('links', tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.Link', blank=True)),
                ('organization', models.ManyToManyField(related_name='member', through='tx_people.Membership', to='tx_people.Organization')),
                ('other_name', tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.OtherNames', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('end_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(max_length=250, null=True, blank=True)),
                ('role', models.CharField(max_length=250, null=True, blank=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(related_name='posts', to='tx_people.ContactDetail', blank=True)),
                ('links', tx_people.fields.OptionalManyToManyField(related_name='posts', to='tx_people.Link', blank=True)),
                ('organization', models.ForeignKey(related_name='posts', to='tx_people.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(related_name='posts', to='tx_people.Source', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='races',
            field=tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.Race', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(related_name='people', to='tx_people.Source', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='other_name',
            field=tx_people.fields.OptionalManyToManyField(related_name='organizations', to='tx_people.OtherNames', blank=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='tx_people.Organization', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(related_name='organizations', to='tx_people.Source', blank=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(related_name='members', to='tx_people.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(related_name='memberships', to='tx_people.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(related_name='members', blank=True, to='tx_people.Post', null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(related_name='memberships', to='tx_people.Source', blank=True),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(related_name='contact_detail', to='tx_people.Source', blank=True),
        ),
    ]
