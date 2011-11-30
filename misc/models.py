from django.db import models
from odm.conventions.util import DBI_get, DBI_records

# =====================================
class EnergyReconVldManager(models.Manager):
    
    def records(self, site, detector, task=0, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'energyrecon', site, detector, task, sim, character, width)
        return output
    

class Energyreconvld(models.Model):
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
    
    objects = EnergyReconVldManager()
    
    class Meta:
        db_table = u'EnergyReconVld'
        ordering = ['-seqno']
    
    def __unicode__(self):
        return u'seq %d' % (self.seqno, )

                
class Energyrecon(models.Model):
    vld = models.ForeignKey(Energyreconvld, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Fake pk, will duplicate
    peevis = models.FloatField(null=True, db_column='PEEVIS', blank=True) # Field name made lowercase.
    peevisunc = models.FloatField(null=True, db_column='PEEVISUNC', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'EnergyRecon'
    
    def __unicode__(self):
        return u'%s: %.2f' % (self.vld, self.peevis)

