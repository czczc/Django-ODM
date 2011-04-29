# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Renaming column for 'Run.runno' to match new field type.
        db.rename_column('odmrun_run', 'runNo', 'runno')
        # Changing field 'Run.runno'
        db.alter_column('odmrun_run', 'runno', self.gf('django.db.models.fields.IntegerField')(unique=True))

        # Adding unique constraint on 'Run', fields ['runno']
        db.create_unique('odmrun_run', ['runno'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Run', fields ['runno']
        db.delete_unique('odmrun_run', ['runno'])

        # Renaming column for 'Run.runno' to match new field type.
        db.rename_column('odmrun_run', 'runno', 'runNo')
        # Changing field 'Run.runno'
        db.alter_column('odmrun_run', 'runNo', self.gf('django.db.models.fields.IntegerField')(db_column='runNo'))


    models = {
        'odmrun.run': {
            'Meta': {'ordering': "['-runno']", 'object_name': 'Run'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runno': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'runtype': ('django.db.models.fields.CharField', [], {'max_length': '96'}),
            'timeend': ('django.db.models.fields.DateTimeField', [], {}),
            'timestart': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['odmrun']
