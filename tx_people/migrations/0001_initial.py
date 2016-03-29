# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tx_people.fields
import tx_people.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.CharField(max_length=250)),
                ('value', models.CharField(max_length=250)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=250)),
                ('scheme', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('end_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(blank=True, related_name='memberships', to='tx_people.ContactDetail')),
                ('links', tx_people.fields.OptionalManyToManyField(blank=True, related_name='memberships', to='tx_people.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('classification', models.CharField(blank=True, max_length=250, null=True)),
                ('founding_date', tx_people.fields.ReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('dissolution_date', tx_people.fields.ReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('contact_details', tx_people.fields.OptionalManyToManyField(blank=True, related_name='organizations', to='tx_people.ContactDetail')),
                ('identifiers', tx_people.fields.OptionalManyToManyField(blank=True, related_name='organizations', to='tx_people.Identifier')),
                ('links', tx_people.fields.OptionalManyToManyField(blank=True, related_name='organizations', to='tx_people.Link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('family_name', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('given_name', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('additional_name', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('honorific_prefix', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('honorific_suffix', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('patronymic_name', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('sort_name', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('email', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('gender', tx_people.fields.OptionalCharField(blank=True, max_length=10, null=True)),
                ('birth_date', tx_people.fields.OptionalReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('death_date', tx_people.fields.OptionalReducedDateField(blank=True, max_length=10, null=True, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'tx_people/')),
                ('summary', tx_people.fields.OptionalCharField(blank=True, max_length=250, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.ContactDetail')),
                ('ethnicities', tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.Ethnicity')),
                ('identifiers', tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.Identifier')),
                ('links', tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.Link')),
                ('organization', models.ManyToManyField(related_name='member', through='tx_people.Membership', to='tx_people.Organization')),
                ('other_name', tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.OtherNames')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('end_date', tx_people.fields.ReducedDateField(max_length=10, validators=[tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator(), tx_people.utils.ReducedDateValidator()])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(blank=True, max_length=250, null=True)),
                ('role', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_details', tx_people.fields.OptionalManyToManyField(blank=True, related_name='posts', to='tx_people.ContactDetail')),
                ('links', tx_people.fields.OptionalManyToManyField(blank=True, related_name='posts', to='tx_people.Link')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='tx_people.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='posts', to='tx_people.Source'),
        ),
        migrations.AddField(
            model_name='person',
            name='races',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.Race'),
        ),
        migrations.AddField(
            model_name='person',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='people', to='tx_people.Source'),
        ),
        migrations.AddField(
            model_name='organization',
            name='other_name',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='organizations', to='tx_people.OtherNames'),
        ),
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tx_people.Organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='organizations', to='tx_people.Source'),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='tx_people.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='tx_people.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='tx_people.Post'),
        ),
        migrations.AddField(
            model_name='membership',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='memberships', to='tx_people.Source'),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='sources',
            field=tx_people.fields.OptionalManyToManyField(blank=True, related_name='contact_detail', to='tx_people.Source'),
        ),
    ]
