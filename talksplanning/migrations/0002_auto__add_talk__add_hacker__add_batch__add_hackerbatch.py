# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Talk'
        db.create_table(u'talksplanning_talk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('speaker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talksplanning.Hacker'])),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talksplanning.Batch'])),
        ))
        db.send_create_signal(u'talksplanning', ['Talk'])

        # Adding model 'Hacker'
        db.create_table(u'talksplanning_hacker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pseudo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('haum', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'talksplanning', ['Hacker'])

        # Adding model 'Batch'
        db.create_table(u'talksplanning_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('theme', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('interne', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'talksplanning', ['Batch'])

        # Adding model 'HackerBatch'
        db.create_table(u'talksplanning_hackerbatch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auditeur', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('orateur', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talksplanning.Batch'])),
            ('hacker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['talksplanning.Hacker'])),
        ))
        db.send_create_signal(u'talksplanning', ['HackerBatch'])


    def backwards(self, orm):
        # Deleting model 'Talk'
        db.delete_table(u'talksplanning_talk')

        # Deleting model 'Hacker'
        db.delete_table(u'talksplanning_hacker')

        # Deleting model 'Batch'
        db.delete_table(u'talksplanning_batch')

        # Deleting model 'HackerBatch'
        db.delete_table(u'talksplanning_hackerbatch')


    models = {
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
        },
        u'talksplanning.batch': {
            'Meta': {'object_name': 'Batch'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['talksplanning.Hacker']", 'through': u"orm['talksplanning.HackerBatch']", 'symmetrical': 'False'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'talksplanning.hacker': {
            'Meta': {'object_name': 'Hacker'},
            'haum': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'pseudo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'talksplanning.hackerbatch': {
            'Meta': {'object_name': 'HackerBatch'},
            'auditeur': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talksplanning.Batch']"}),
            'hacker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talksplanning.Hacker']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orateur': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'talksplanning.talk': {
            'Meta': {'object_name': 'Talk'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talksplanning.Batch']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['talksplanning.Hacker']"}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['talksplanning']