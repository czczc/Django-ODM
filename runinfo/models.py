from django.db import models
from django.conf import settings

import datetime

class RuninfoManager(models.Manager):
    def list_runtype(self, runtype):
        if runtype == 'All':
            return self.select_related()
        return self.select_related().filter(runtype=runtype)

#=====================================
class Daqruninfovld(models.Model):
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
        db_table = u'DaqRunInfoVld'
        ordering = ['-seqno']
    
    def __unicode__(self):
        return u'seq %d' % (self.seqno, )
    
    def runlength(self):
        return self.timeend - self.timestart
    
    def timestart_beijing(self):
        return self.timestart + datetime.timedelta(seconds=8*3600)   

    def timeend_beijing(self):
        return self.timeend + datetime.timedelta(seconds=8*3600)

#=====================================
class Daqruninfo(models.Model):
    vld = models.ForeignKey(Daqruninfovld, primary_key=True, db_column='SEQNO') # Field name made lowercase.
    # row_counter = models.IntegerField(db_column='ROW_COUNTER') # not useful.
    runno = models.IntegerField(db_column='runNo') # Field name made lowercase.
    # triggertype = models.BigIntegerField(null=True, db_column='triggerType', blank=True) # not useful.
    runtype = models.CharField(max_length=96, db_column='runType', blank=True) # Field name made lowercase.
    detectormask = models.IntegerField(null=True, db_column='detectorMask', blank=True) # Field name made lowercase.
    partitionname = models.CharField(max_length=765, db_column='partitionName', blank=True) # Field name made lowercase.
    schemaversion = models.IntegerField(null=True, db_column='schemaVersion', blank=True) # Field name made lowercase.
    dataversion = models.IntegerField(null=True, db_column='dataVersion', blank=True) # Field name made lowercase.
    baseversion = models.IntegerField(null=True, db_column='baseVersion', blank=True) # Field name made lowercase.
    
    objects = RuninfoManager()
    
    class Meta:
        db_table = u'DaqRunInfo'
        ordering = ['-runno']
        
    def __unicode__(self):
        return u'run %d' % (self.runno, )
    
    def get_absolute_url(self):
        return "%s/run/%i/" % (settings.SITE_ROOT, self.runno)

# =====================================
class Daqcalibruninfo(models.Model):
    seqno = models.IntegerField(primary_key=True, db_column='SEQNO') # Field name made lowercase.
    # row_counter = models.IntegerField(db_column='ROW_COUNTER') # not useful.
    runno = models.IntegerField(db_column='runNo') # Field name made lowercase.
    adno = models.IntegerField(null=True, db_column='AdNo', blank=True) # Field name made lowercase.
    detectorid = models.IntegerField(null=True, db_column='detectorId', blank=True) # Field name made lowercase.
    sourceida = models.IntegerField(null=True, db_column='sourceIdA', blank=True) # Field name made lowercase.
    zpositiona = models.IntegerField(null=True, db_column='zPositionA', blank=True) # Field name made lowercase.
    sourceidb = models.IntegerField(null=True, db_column='sourceIdB', blank=True) # Field name made lowercase.
    zpositionb = models.IntegerField(null=True, db_column='zPositionB', blank=True) # Field name made lowercase.
    sourceidc = models.IntegerField(null=True, db_column='sourceIdC', blank=True) # Field name made lowercase.
    zpositionc = models.IntegerField(null=True, db_column='zPositionC', blank=True) # Field name made lowercase.
    duration = models.IntegerField(null=True, blank=True)
    lednumber1 = models.IntegerField(null=True, db_column='ledNumber1', blank=True) # Field name made lowercase.
    lednumber2 = models.IntegerField(null=True, db_column='ledNumber2', blank=True) # Field name made lowercase.
    ledvoltage1 = models.IntegerField(null=True, db_column='ledVoltage1', blank=True) # Field name made lowercase.
    ledvoltage2 = models.IntegerField(null=True, db_column='ledVoltage2', blank=True) # Field name made lowercase.
    ledfreq = models.IntegerField(null=True, db_column='ledFreq', blank=True) # Field name made lowercase.
    ledpulsesep = models.IntegerField(null=True, db_column='ledPulseSep', blank=True) # Field name made lowercase.
    ltbmode = models.IntegerField(null=True, db_column='ltbMode', blank=True) # Field name made lowercase.
    homea = models.IntegerField(null=True, db_column='HomeA', blank=True) # Field name made lowercase.
    homeb = models.IntegerField(null=True, db_column='HomeB', blank=True) # Field name made lowercase.
    homec = models.IntegerField(null=True, db_column='HomeC', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'DaqCalibRunInfo'
        ordering = ['-runno']
    
    def __unicode__(self):
        return u'calib run %d' % (self.runno, )
        