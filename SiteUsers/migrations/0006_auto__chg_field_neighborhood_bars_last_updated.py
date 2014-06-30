# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Neighborhood.bars_last_updated'
        db.alter_column(u'SiteUsers_neighborhood', 'bars_last_updated', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Neighborhood.bars_last_updated'
        db.alter_column(u'SiteUsers_neighborhood', 'bars_last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True))

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