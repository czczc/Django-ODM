from django.db import models
from datetime import timedelta

# Create your models here.
class Dataqualitypmtvld(models.Model):
    seqno = models.IntegerField(primary_key=True, db_column='SEQNO') # Field name made lowercase.
    timestart = models.DateTimeField(db_column='TIMESTART') # Field name made lowercase.
    timeend = models.DateTimeField(db_column='TIMEEND') # Field name made lowercase.
    sitemask = models.IntegerField(null=True, db_column='SITEMASK', blank=True) # Field name made lowercase.
    simmask = models.IntegerField(null=True, db_column='SIMMASK', blank=True) # Field name made lowercase.
    subsite = models.IntegerField(null=True, db_column='SUBSITE', blank=True) # Field name made lowercase.
    task = models.IntegerField(null=True, db_column='TASK', blank=True) # Field name made lowercase.
    aggregateno = models.IntegerField(null=True, db_column='AGGREGATENO', blank=True) # Field name made lowercase.
    versiondate = models.DateTimeField(db_column='VERSIONDATE') # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='INSERTDATE') # Field name made lowercase.
    class Meta:
        db_table = u'DataQualityPmtVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )

    def timestart_beijing(self):
        return self.timestart + timedelta(seconds=8*3600)

                
class Dataqualitypmt(models.Model):
    vld = models.ForeignKey(Dataqualitypmtvld, db_column='SEQNO') # Field name made lowercase.        
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Field name made lowercase.
    runno = models.IntegerField(null=True, db_column='RUNNO', blank=True) # Field name made lowercase.
    fileno = models.IntegerField(null=True, db_column='FILENO', blank=True) # Field name made lowercase.
    pmtid = models.IntegerField(null=True, db_column='PMTID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    chi2ndf = models.FloatField(null=True, db_column='CHI2NDF', blank=True) # Field name made lowercase.
    gain = models.FloatField(null=True, db_column='GAIN', blank=True) # Field name made lowercase.
    gainerr = models.FloatField(null=True, db_column='GAINERR', blank=True) # Field name made lowercase.
    darkrate = models.FloatField(null=True, db_column='DARKRATE', blank=True) # Field name made lowercase.
    darkrateerr = models.FloatField(null=True, db_column='DARKRATEERR', blank=True) # Field name made lowercase.
    elecnoiserate = models.FloatField(null=True, db_column='ELECNOISERATE', blank=True) # Field name made lowercase.
    elecnoiserateerr = models.FloatField(null=True, db_column='ELECNOISERATEERR', blank=True) # Field name made lowercase.
    preadc = models.FloatField(null=True, db_column='PREADC', blank=True) # Field name made lowercase.
    preadcerr = models.FloatField(null=True, db_column='PREADCERR', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DataQualityPmt'
        ordering = ['-runno', 'fileno']
    
    def __unicode__(self):
        return u'run %d file %d' % (self.runno, self.fileno)        

