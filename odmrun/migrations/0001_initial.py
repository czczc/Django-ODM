# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Run'
        db.create_table('odmrun_run', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('runno', self.gf('django.db.models.fields.IntegerField')(db_column='runNo')),
            ('runtype', self.gf('django.db.models.fields.CharField')(max_length=96)),
            ('timestart', self.gf('django.db.models.fields.DateTimeField')()),
            ('timeend', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('odmrun', ['Run'])


    def backwards(self, orm):
        
        # Deleting model 'Run'
        db.delete_table('odmrun_run')


    models = {
        'odmrun.run': {
            'Meta': {'ordering': "['-runno']", 'object_name': 'Run'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runno': ('django.db.models.fields.IntegerField', [], {'db_column': "'runNo'"}),
            'runtype': ('django.db.models.fields.CharField', [], {'max_length': '96'}),
            'timeend': ('django.db.models.fields.DateTimeField', [], {}),
            'timestart': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['odmrun']
