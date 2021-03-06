# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'SiteUsers_userprofile', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('fb_token', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('ig_token', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
            ('ig_username', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('ig_pic', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('ig_follows', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ig_followers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.City'], null=True)),
            ('birthyear', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal(u'SiteUsers', ['UserProfile'])

        # Adding model 'Friends'
        db.create_table(u'SiteUsers_friends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person', to=orm['SiteUsers.UserProfile'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friend', to=orm['SiteUsers.UserProfile'])),
        ))
        db.send_create_signal(u'SiteUsers', ['Friends'])

        # Adding unique constraint on 'Friends', fields ['person', 'friend']
        db.create_unique(u'SiteUsers_friends', ['person_id', 'friend_id'])

        # Adding model 'Education'
        db.create_table(u'SiteUsers_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.UserProfile'])),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.School'])),
        ))
        db.send_create_signal(u'SiteUsers', ['Education'])

        # Adding model 'City'
        db.create_table(u'SiteUsers_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'SiteUsers', ['City'])

        # Adding model 'Neighborhood'
        db.create_table(u'SiteUsers_neighborhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neighborhood_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.City'])),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lng', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bars_last_updated', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'SiteUsers', ['Neighborhood'])

        # Adding model 'School'
        db.create_table(u'SiteUsers_school', (
            ('school_id', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('school_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'SiteUsers', ['School'])


    def backwards(self, orm):
        # Removing unique constraint on 'Friends', fields ['person', 'friend']
        db.delete_unique(u'SiteUsers_friends', ['person_id', 'friend_id'])

        # Deleting model 'UserProfile'
        db.delete_table(u'SiteUsers_userprofile')

        # Deleting model 'Friends'
        db.delete_table(u'SiteUsers_friends')

        # Deleting model 'Education'
        db.delete_table(u'SiteUsers_education')

        # Deleting model 'City'
        db.delete_table(u'SiteUsers_city')

        # Deleting model 'Neighborhood'
        db.delete_table(u'SiteUsers_neighborhood')

        # Deleting model 'School'
        db.delete_table(u'SiteUsers_school')


    models = {
        u'SiteUsers.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'SiteUsers.education': {
            'Meta': {'object_name': 'Education'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.School']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.UserProfile']"})
        },
        u'SiteUsers.friends': {
            'Meta': {'unique_together': "(('person', 'friend'),)", 'object_name': 'Friends'},
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friend'", 'to': u"orm['SiteUsers.UserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person'", 'to': u"orm['SiteUsers.UserProfile']"})
        },
        u'SiteUsers.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'bars_last_updated': ('django.db.models.fields.DateField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'neighborhood_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'SiteUsers.school': {
            'Meta': {'object_name': 'School'},
            'school_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'school_type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'SiteUsers.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.City']", 'null': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'fb_token': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'ig_followers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ig_follows': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ig_pic': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'ig_token': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'ig_username': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['SiteUsers']