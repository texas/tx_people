# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OtherNames'
        db.create_table(u'tx_people_othernames', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tx_people', ['OtherNames'])

        # Adding model 'Identifier'
        db.create_table(u'tx_people_identifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('scheme', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'tx_people', ['Identifier'])

        # Adding model 'Link'
        db.create_table(u'tx_people_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tx_people', ['Link'])

        # Adding model 'Source'
        db.create_table(u'tx_people_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'tx_people', ['Source'])

        # Adding model 'ContactDetail'
        db.create_table(u'tx_people_contactdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tx_people', ['ContactDetail'])

        # Adding M2M table for field sources on 'ContactDetail'
        m2m_table_name = db.shorten_name(u'tx_people_contactdetail_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contactdetail', models.ForeignKey(orm[u'tx_people.contactdetail'], null=False)),
            ('source', models.ForeignKey(orm[u'tx_people.source'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contactdetail_id', 'source_id'])

        # Adding model 'Organization'
        db.create_table(u'tx_people_organization', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['tx_people.Organization'])),
            ('founding_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10, null=True, blank=True)),
            ('dissolution_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'tx_people', ['Organization'])

        # Adding M2M table for field other_name on 'Organization'
        m2m_table_name = db.shorten_name(u'tx_people_organization_other_name')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'tx_people.organization'], null=False)),
            ('othernames', models.ForeignKey(orm[u'tx_people.othernames'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'othernames_id'])

        # Adding M2M table for field identifiers on 'Organization'
        m2m_table_name = db.shorten_name(u'tx_people_organization_identifiers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'tx_people.organization'], null=False)),
            ('identifier', models.ForeignKey(orm[u'tx_people.identifier'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'identifier_id'])

        # Adding M2M table for field contact_details on 'Organization'
        m2m_table_name = db.shorten_name(u'tx_people_organization_contact_details')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'tx_people.organization'], null=False)),
            ('contactdetail', models.ForeignKey(orm[u'tx_people.contactdetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'contactdetail_id'])

        # Adding M2M table for field links on 'Organization'
        m2m_table_name = db.shorten_name(u'tx_people_organization_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'tx_people.organization'], null=False)),
            ('link', models.ForeignKey(orm[u'tx_people.link'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'link_id'])

        # Adding M2M table for field sources on 'Organization'
        m2m_table_name = db.shorten_name(u'tx_people_organization_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'tx_people.organization'], null=False)),
            ('source', models.ForeignKey(orm[u'tx_people.source'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'source_id'])

        # Adding model 'Post'
        db.create_table(u'tx_people_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10)),
            ('end_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['tx_people.Organization'])),
        ))
        db.send_create_signal(u'tx_people', ['Post'])

        # Adding M2M table for field contact_details on 'Post'
        m2m_table_name = db.shorten_name(u'tx_people_post_contact_details')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'tx_people.post'], null=False)),
            ('contactdetail', models.ForeignKey(orm[u'tx_people.contactdetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'contactdetail_id'])

        # Adding M2M table for field links on 'Post'
        m2m_table_name = db.shorten_name(u'tx_people_post_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'tx_people.post'], null=False)),
            ('link', models.ForeignKey(orm[u'tx_people.link'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'link_id'])

        # Adding M2M table for field sources on 'Post'
        m2m_table_name = db.shorten_name(u'tx_people_post_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'tx_people.post'], null=False)),
            ('source', models.ForeignKey(orm[u'tx_people.source'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'source_id'])

        # Adding model 'Membership'
        db.create_table(u'tx_people_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10)),
            ('end_date', self.gf('tx_people.fields.ReducedDateField')(max_length=10)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='memberships', to=orm['tx_people.Person'])),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', to=orm['tx_people.Organization'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='members', null=True, to=orm['tx_people.Post'])),
        ))
        db.send_create_signal(u'tx_people', ['Membership'])

        # Adding M2M table for field contact_details on 'Membership'
        m2m_table_name = db.shorten_name(u'tx_people_membership_contact_details')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membership', models.ForeignKey(orm[u'tx_people.membership'], null=False)),
            ('contactdetail', models.ForeignKey(orm[u'tx_people.contactdetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['membership_id', 'contactdetail_id'])

        # Adding M2M table for field links on 'Membership'
        m2m_table_name = db.shorten_name(u'tx_people_membership_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membership', models.ForeignKey(orm[u'tx_people.membership'], null=False)),
            ('link', models.ForeignKey(orm[u'tx_people.link'], null=False))
        ))
        db.create_unique(m2m_table_name, ['membership_id', 'link_id'])

        # Adding M2M table for field sources on 'Membership'
        m2m_table_name = db.shorten_name(u'tx_people_membership_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membership', models.ForeignKey(orm[u'tx_people.membership'], null=False)),
            ('source', models.ForeignKey(orm[u'tx_people.source'], null=False))
        ))
        db.create_unique(m2m_table_name, ['membership_id', 'source_id'])

        # Adding model 'Person'
        db.create_table(u'tx_people_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('family_name', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('given_name', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('additional_name', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('honorific_prefix', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('honorific_suffix', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('patronymic_name', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('sort_name', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('email', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('gender', self.gf('tx_people.fields.OptionalCharField')(max_length=10, null=True, blank=True)),
            ('birth_date', self.gf('tx_people.fields.OptionalReducedDateField')(max_length=10, null=True, blank=True)),
            ('death_date', self.gf('tx_people.fields.OptionalReducedDateField')(max_length=10, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('summary', self.gf('tx_people.fields.OptionalCharField')(max_length=250, null=True, blank=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tx_people', ['Person'])

        # Adding M2M table for field other_name on 'Person'
        m2m_table_name = db.shorten_name(u'tx_people_person_other_name')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'tx_people.person'], null=False)),
            ('othernames', models.ForeignKey(orm[u'tx_people.othernames'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'othernames_id'])

        # Adding M2M table for field identifiers on 'Person'
        m2m_table_name = db.shorten_name(u'tx_people_person_identifiers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'tx_people.person'], null=False)),
            ('identifier', models.ForeignKey(orm[u'tx_people.identifier'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'identifier_id'])

        # Adding M2M table for field contact_details on 'Person'
        m2m_table_name = db.shorten_name(u'tx_people_person_contact_details')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'tx_people.person'], null=False)),
            ('contactdetail', models.ForeignKey(orm[u'tx_people.contactdetail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'contactdetail_id'])

        # Adding M2M table for field links on 'Person'
        m2m_table_name = db.shorten_name(u'tx_people_person_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'tx_people.person'], null=False)),
            ('link', models.ForeignKey(orm[u'tx_people.link'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'link_id'])

        # Adding M2M table for field sources on 'Person'
        m2m_table_name = db.shorten_name(u'tx_people_person_sources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'tx_people.person'], null=False)),
            ('source', models.ForeignKey(orm[u'tx_people.source'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'source_id'])


    def backwards(self, orm):
        # Deleting model 'OtherNames'
        db.delete_table(u'tx_people_othernames')

        # Deleting model 'Identifier'
        db.delete_table(u'tx_people_identifier')

        # Deleting model 'Link'
        db.delete_table(u'tx_people_link')

        # Deleting model 'Source'
        db.delete_table(u'tx_people_source')

        # Deleting model 'ContactDetail'
        db.delete_table(u'tx_people_contactdetail')

        # Removing M2M table for field sources on 'ContactDetail'
        db.delete_table(db.shorten_name(u'tx_people_contactdetail_sources'))

        # Deleting model 'Organization'
        db.delete_table(u'tx_people_organization')

        # Removing M2M table for field other_name on 'Organization'
        db.delete_table(db.shorten_name(u'tx_people_organization_other_name'))

        # Removing M2M table for field identifiers on 'Organization'
        db.delete_table(db.shorten_name(u'tx_people_organization_identifiers'))

        # Removing M2M table for field contact_details on 'Organization'
        db.delete_table(db.shorten_name(u'tx_people_organization_contact_details'))

        # Removing M2M table for field links on 'Organization'
        db.delete_table(db.shorten_name(u'tx_people_organization_links'))

        # Removing M2M table for field sources on 'Organization'
        db.delete_table(db.shorten_name(u'tx_people_organization_sources'))

        # Deleting model 'Post'
        db.delete_table(u'tx_people_post')

        # Removing M2M table for field contact_details on 'Post'
        db.delete_table(db.shorten_name(u'tx_people_post_contact_details'))

        # Removing M2M table for field links on 'Post'
        db.delete_table(db.shorten_name(u'tx_people_post_links'))

        # Removing M2M table for field sources on 'Post'
        db.delete_table(db.shorten_name(u'tx_people_post_sources'))

        # Deleting model 'Membership'
        db.delete_table(u'tx_people_membership')

        # Removing M2M table for field contact_details on 'Membership'
        db.delete_table(db.shorten_name(u'tx_people_membership_contact_details'))

        # Removing M2M table for field links on 'Membership'
        db.delete_table(db.shorten_name(u'tx_people_membership_links'))

        # Removing M2M table for field sources on 'Membership'
        db.delete_table(db.shorten_name(u'tx_people_membership_sources'))

        # Deleting model 'Person'
        db.delete_table(u'tx_people_person')

        # Removing M2M table for field other_name on 'Person'
        db.delete_table(db.shorten_name(u'tx_people_person_other_name'))

        # Removing M2M table for field identifiers on 'Person'
        db.delete_table(db.shorten_name(u'tx_people_person_identifiers'))

        # Removing M2M table for field contact_details on 'Person'
        db.delete_table(db.shorten_name(u'tx_people_person_contact_details'))

        # Removing M2M table for field links on 'Person'
        db.delete_table(db.shorten_name(u'tx_people_person_links'))

        # Removing M2M table for field sources on 'Person'
        db.delete_table(db.shorten_name(u'tx_people_person_sources'))


    models = {
        u'tx_people.contactdetail': {
            'Meta': {'object_name': 'ContactDetail'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sources': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'contact_detail'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Source']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'tx_people.identifier': {
            'Meta': {'object_name': 'Identifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'scheme': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'tx_people.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'tx_people.membership': {
            'Meta': {'object_name': 'Membership'},
            'contact_details': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'memberships'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.ContactDetail']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'end_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'links': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'memberships'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Link']"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': u"orm['tx_people.Organization']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': u"orm['tx_people.Person']"}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': u"orm['tx_people.Post']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sources': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'memberships'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Source']"}),
            'start_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'tx_people.organization': {
            'Meta': {'object_name': 'Organization'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'contact_details': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'organizations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.ContactDetail']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'dissolution_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'founding_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifiers': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'organizations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Identifier']"}),
            'links': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'organizations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Link']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'other_name': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'organizations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.OtherNames']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['tx_people.Organization']"}),
            'sources': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'organizations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Source']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'tx_people.othernames': {
            'Meta': {'object_name': 'OtherNames'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tx_people.person': {
            'Meta': {'object_name': 'Person'},
            'additional_name': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('tx_people.fields.OptionalReducedDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'contact_details': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.ContactDetail']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'death_date': ('tx_people.fields.OptionalReducedDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'email': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'family_name': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'gender': ('tx_people.fields.OptionalCharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'given_name': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'honorific_prefix': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'honorific_suffix': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifiers': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Identifier']"}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'links': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Link']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'organization': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'member'", 'symmetrical': 'False', 'through': u"orm['tx_people.Membership']", 'to': u"orm['tx_people.Organization']"}),
            'other_name': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.OtherNames']"}),
            'patronymic_name': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sort_name': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sources': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'people'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Source']"}),
            'summary': ('tx_people.fields.OptionalCharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'tx_people.post': {
            'Meta': {'object_name': 'Post'},
            'contact_details': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'posts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.ContactDetail']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'end_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'links': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'posts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Link']"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['tx_people.Organization']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sources': ('tx_people.fields.OptionalManyToManyField', [], {'blank': 'True', 'related_name': "'posts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tx_people.Source']"}),
            'start_date': ('tx_people.fields.ReducedDateField', [], {'max_length': '10'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'tx_people.source': {
            'Meta': {'object_name': 'Source'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['tx_people']