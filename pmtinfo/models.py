from django.db import models
from odm.conventions.util import DBI_get
from odm.conventions.conf import Site, Detector

# =====================================
class FeeCableMapManager(models.Manager):
    
    def cablemapSet(self, year, month, day, site, detector):
        '''Returns a QuerySet of DBI Feecablemap'''
        
        vld = DBI_get(self.select_related(), {
            'year' : int(year),
            'month' : int(month),
            'day' : int(day),
            'site' : Site.site_id[site],
            'detector' : Detector.detector_id[detector],
        })
        if vld:
            return vld.feecablemap_set
        else:
            return None

# =====================================
class CalibPMTSpecManager(models.Manager):
    
    def pmtspecSet(self, year, month, day, site, detector):
        '''Returns a QuerySet of DBI Calibpmtspec'''
        
        vld = DBI_get(self.select_related(), {
            'year' : int(year),
            'month' : int(month),
            'day' : int(day),
            'site' : site,
            'detector' : detector,
        })
        if vld:
            return vld.calibpmtspec_set
        else:
            return None
            

# =====================================
class Feecablemapvld(models.Model):
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
    
    objects = FeeCableMapManager()
    
    class Meta:
        db_table = u'FeeCableMapVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )
 
        
# =====================================
class Feecablemap(models.Model):
    vld = models.ForeignKey(Feecablemapvld, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Fake pk, will duplicate (legacy db use multiple fields as pk)
    feechannelid = models.IntegerField(null=True, db_column='FEECHANNELID', blank=True) # Field name made lowercase.
    feechanneldesc = models.CharField(max_length=90, db_column='FEECHANNELDESC', blank=True) # Field name made lowercase.
    feehardwareid = models.IntegerField(null=True, db_column='FEEHARDWAREID', blank=True) # Field name made lowercase.
    chanhrdwdesc = models.CharField(max_length=90, db_column='CHANHRDWDESC', blank=True) # Field name made lowercase.
    sensorid = models.IntegerField(null=True, db_column='SENSORID', blank=True) # Field name made lowercase.
    sensordesc = models.CharField(max_length=90, db_column='SENSORDESC', blank=True) # Field name made lowercase.
    pmthardwareid = models.IntegerField(null=True, db_column='PMTHARDWAREID', blank=True) # Field name made lowercase.
    pmthrdwdesc = models.CharField(max_length=90, db_column='PMTHRDWDESC', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'FeeCableMap'
        ordering = ['row_counter']

    def __unicode__(self):
        return self.feechanneldesc


# =====================================
class Calibpmtspecvld(models.Model):
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
    
    objects = CalibPMTSpecManager()
    
    class Meta:
        db_table = u'CalibPmtSpecVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )        
        
        
# =====================================
class Calibpmtspec(models.Model):
    vld = models.ForeignKey(Calibpmtspecvld, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Field name made lowercase.
    pmtid = models.IntegerField(null=True, db_column='PMTID', blank=True) # Field name made lowercase.
    pmtdescrib = models.CharField(max_length=81, db_column='PMTDESCRIB', blank=True) # Field name made lowercase.
    pmtstatus = models.IntegerField(null=True, db_column='PMTSTATUS', blank=True) # Field name made lowercase.
    pmtspehigh = models.FloatField(null=True, db_column='PMTSPEHIGH', blank=True) # Field name made lowercase.
    pmtsigmaspehigh = models.FloatField(null=True, db_column='PMTSIGMASPEHIGH', blank=True) # Field name made lowercase.
    pmtspelow = models.FloatField(null=True, db_column='PMTSPELOW', blank=True) # Field name made lowercase.
    pmttoffset = models.FloatField(null=True, db_column='PMTTOFFSET', blank=True) # Field name made lowercase.
    pmttspread = models.FloatField(null=True, db_column='PMTTSPREAD', blank=True) # Field name made lowercase.
    pmteffic = models.FloatField(null=True, db_column='PMTEFFIC', blank=True) # Field name made lowercase.
    pmtprepulse = models.FloatField(null=True, db_column='PMTPREPULSE', blank=True) # Field name made lowercase.
    pmtafterpulse = models.FloatField(null=True, db_column='PMTAFTERPULSE', blank=True) # Field name made lowercase.
    pmtdarkrate = models.FloatField(null=True, db_column='PMTDARKRATE', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'CalibPmtSpec'
        ordering = ['row_counter']

    def __unicode__(self):
        return self.pmtdescrib


