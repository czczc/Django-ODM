from django.db import models
from odm.conventions.util import DBI_get, DBI_records, DBI_trend

# =====================================
class EnergyreconvldManager(models.Manager):
    
    def records(self, site, detector, task=0, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'energyrecon', site, detector, task, sim, character, width)
        return output


# =====================================
class EnergyreconManager(models.Manager):
    
    def trend(self, site, detector, task=0, sim=1):
        '''Returns correct dbi values as a funtion of time'''
                
        dbi_records = DBI_trend(self.select_related(), site, detector, task, sim)
        values = [] 
        for key in sorted(dbi_records):
            value = dbi_records[key]
            values.append({
                'start' : str(key),
                'end' : str(value['end']),
                'seqno' : value['record'].vld.seqno,
                'timestart' : str(value['record'].vld.timestart),
                'timeend' : str(value['record'].vld.timeend),
                'insertdate' : str(value['record'].vld.insertdate),
                'versiondate' : str(value['record'].vld.versiondate),
                'peevis' : value['record'].peevis,
                'peevisunc' : value['record'].peevisunc,
            })
        return values    


# =====================================
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
    
    objects = EnergyreconvldManager()
    
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
    
    objects = EnergyreconManager()
    
    class Meta:
        db_table = u'EnergyRecon'
    
    def __unicode__(self):
        return u'%s: %.2f' % (self.vld, self.peevis)

