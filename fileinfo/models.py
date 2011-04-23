from django.db import models
from datetime import timedelta

class Daqrawdatafileinfovld(models.Model):
    seqno = models.IntegerField(primary_key=True, db_column='SEQNO') # Field name made lowercase.
    timestart = models.DateTimeField(db_column='TIMESTART') # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TIMEEND') # Field name made lowercase.
    sitemask = models.IntegerField(db_column='SITEMASK') # Field name made lowercase.
    simmask = models.IntegerField(db_column='SIMMASK') # Field name made lowercase.
    subsite = models.IntegerField(db_column='SUBSITE') # Field name made lowercase.
    task = models.IntegerField(db_column='TASK') # Field name made lowercase.
    aggregateno = models.IntegerField(null=True, db_column='AGGREGATENO', blank=True) # Field name made lowercase.
    versiondate = models.DateTimeField(null=True, db_column='VERSIONDATE', blank=True) # Field name made lowercase.
    insertdate = models.DateTimeField(null=True, db_column='INSERTDATE', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'DaqRawDataFileInfoVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )

    def timeend_beijing(self):
        return self.timeend + timedelta(seconds=8*3600)

    def timeend_pst(self):
        return self.timeend + timedelta(seconds=-8*3600)
        
class Daqrawdatafileinfo(models.Model):
    vld = models.ForeignKey(Daqrawdatafileinfovld, db_column='SEQNO') # Field name made lowercase.    
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Fake pk, Should be one (per seqno)
    runno = models.IntegerField(null=True, db_column='runNo', blank=True) # Field name made lowercase.
    fileno = models.IntegerField(null=True, db_column='fileNo', blank=True) # Field name made lowercase.
    filename = models.TextField(db_column='fileName', blank=True) # Field name made lowercase.
    streamtype = models.CharField(max_length=96, db_column='streamType', blank=True) # Field name made lowercase.
    stream = models.CharField(max_length=96, blank=True)
    filestate = models.CharField(max_length=96, db_column='fileState', blank=True) # Field name made lowercase.
    filesize = models.IntegerField(null=True, db_column='fileSize', blank=True) # Field name made lowercase.
    checksum = models.CharField(max_length=192, blank=True)
    transferstate = models.CharField(max_length=96, db_column='transferState', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'DaqRawDataFileInfo'
        ordering = ['-runno', 'fileno', 'filename']
    
    def __unicode__(self):
        return u'run %d' % (self.runno, )
    
