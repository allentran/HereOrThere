# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bar'
        db.create_table(u'Rankings_bar', (
            ('FS_id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
<<<<<<< HEAD
            ('IG_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('lng', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal(u'Rankings', ['Bar'])

        # Adding model 'BarLocations'
        db.create_table(u'Rankings_barlocations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rankings.Bar'])),
            ('neighborhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.Neighborhood'])),
        ))
        db.send_create_signal(u'Rankings', ['BarLocations'])

        # Adding model 'PublicLadder'
        db.create_table(u'Rankings_publicladder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.City'])),
=======
        ))
        db.send_create_signal(u'Rankings', ['Bar'])

        # Adding model 'PublicLadder'
        db.create_table(u'Rankings_publicladder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.Location'])),
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'Rankings', ['PublicLadder'])

        # Adding model 'PublicOrdering'
        db.create_table(u'Rankings_publicordering', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ladder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rankings.PublicLadder'])),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rankings.Bar'])),
            ('rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'Rankings', ['PublicOrdering'])

        # Adding model 'Vote'
        db.create_table(u'Rankings_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
<<<<<<< HEAD
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['SiteUsers.UserProfile'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='winner', null=True, to=orm['Rankings.Bar'])),
            ('loser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loser', null=True, to=orm['Rankings.Bar'])),
=======
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='winner', to=orm['Rankings.Bar'])),
            ('loser', self.gf('django.db.models.fields.related.ForeignKey')(related_name='loser', to=orm['Rankings.Bar'])),
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'Rankings', ['Vote'])

<<<<<<< HEAD
        # Adding model 'IGrank'
        db.create_table(u'Rankings_igrank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('bar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Rankings.Bar'])),
            ('total_likes', self.gf('django.db.models.fields.IntegerField')()),
            ('avg_likes', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'Rankings', ['IGrank'])

=======
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5

    def backwards(self, orm):
        # Deleting model 'Bar'
        db.delete_table(u'Rankings_bar')

<<<<<<< HEAD
        # Deleting model 'BarLocations'
        db.delete_table(u'Rankings_barlocations')

=======
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5
        # Deleting model 'PublicLadder'
        db.delete_table(u'Rankings_publicladder')

        # Deleting model 'PublicOrdering'
        db.delete_table(u'Rankings_publicordering')

        # Deleting model 'Vote'
        db.delete_table(u'Rankings_vote')

<<<<<<< HEAD
        # Deleting model 'IGrank'
        db.delete_table(u'Rankings_igrank')

=======
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5

    models = {
        u'Rankings.bar': {
            'FS_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
<<<<<<< HEAD
            'IG_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'Bar'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'Rankings.barlocations': {
            'Meta': {'object_name': 'BarLocations'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rankings.Bar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neighborhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.Neighborhood']"})
        },
        u'Rankings.igrank': {
            'Meta': {'object_name': 'IGrank'},
            'avg_likes': ('django.db.models.fields.FloatField', [], {}),
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rankings.Bar']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_likes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Rankings.publicladder': {
            'Meta': {'object_name': 'PublicLadder'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.City']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
=======
            'Meta': {'object_name': 'Bar'}
        },
        u'Rankings.publicladder': {
            'Meta': {'object_name': 'PublicLadder'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.Location']"})
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5
        },
        u'Rankings.publicordering': {
            'Meta': {'object_name': 'PublicOrdering'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rankings.Bar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ladder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Rankings.PublicLadder']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Rankings.vote': {
            'Meta': {'object_name': 'Vote'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
<<<<<<< HEAD
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loser'", 'null': 'True', 'to': u"orm['Rankings.Bar']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.UserProfile']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winner'", 'null': 'True', 'to': u"orm['Rankings.Bar']"})
        },
        u'SiteUsers.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'SiteUsers.neighborhood': {
            'Meta': {'object_name': 'Neighborhood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['SiteUsers.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'neighborhood_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
=======
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'loser'", 'to': u"orm['Rankings.Bar']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'winner'", 'to': u"orm['Rankings.Bar']"})
        },
        u'SiteUsers.location': {
            'Meta': {'object_name': 'Location'},
            'location_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
>>>>>>> 1a979101ec488e45df196b6bd89ce4a8710b83f5
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

    complete_apps = ['Rankings']