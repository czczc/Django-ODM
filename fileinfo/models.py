from django.db import models

class Daqrawdatafileinfo(models.Model):
    seqno = models.IntegerField(primary_key=True, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Should be one (per seqno)
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
        ordering = ['-runno', 'seqno']
    
    def __unicode__(self):
        return u'run %d' % (self.runno, )
    
