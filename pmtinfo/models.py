from django.db import models
from odm.conventions.util import DBI_get, DBI_records, DBI_trend
from odm.conventions.conf import Site, Detector
from odm.conventions.pmt import SensorId, ChannelId

from datetime import datetime, timedelta        

# =====================================
class CablemapvldManager(models.Manager):
    
    def cablemapSet(self, site, detector, year, month, day,
        rollback=False, rollback_year='', rollback_month='', rollback_day=''):
        '''Returns a QuerySet of DBI Feecablemap'''
        
        try:
            site = Site.site_id[site]
            detector = Detector.detector_id[detector]
        except KeyError:
            return None
        
        context = {
            'year' : int(year),
            'month' : int(month),
            'day' : int(day),
            'site' : site,
            'detector' : detector,
        }
        if rollback:
            context['rollback'] = {
                'year' : int(rollback_year),
                'month' : int(rollback_month),
                'day' : int(rollback_day),
            }
        
        vld = DBI_get(self.select_related(), context)
        if vld:
            return vld.cablemap_set
        else:
            return None


    def records(self, site, detector, task=0, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'cablemap', site, detector, task, sim, character, width)
        return output

# =====================================
class CablemapManager(models.Manager):
    
    def trend(self, site, detector, ring, column, in_out=1, task=0, sim=1):
        '''Returns correct dbi values as a funtion of time'''
        try:
            if detector in ['AD1', 'AD2', 'AD3', 'AD4']:
                sensorid = SensorId.ADfullPackedData(
                    Site.site_id[site], 
                    Detector.detector_id[detector], 
                    ring, column)
            elif detector in ['IWS', 'OWS']:
                sensorid = SensorId.WPfullPackedData(
                    Site.site_id[site], 
                    Detector.detector_id[detector], 
                    ring, column, in_out) # wall = ring, spot = column
            else:
                return []
        except KeyError:
            return []
            
        
        dbi_records = DBI_trend(
            self.select_related().filter(
                sensorid=sensorid,
            ), site, detector, task, sim)
        
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
                'board' : int(value['record'].board()),
                'connector' : int(value['record'].connector()),
            })
            
        return values

# =====================================
class CalibpmtspecvldManager(models.Manager):
    '''Manager'''
    
    def pmtspecSet(self, site, detector, year, month, day,
        rollback=False, rollback_year='', rollback_month='', rollback_day=''):
        '''Returns a QuerySet of DBI Calibpmtspec'''
        try:
            site = Site.site_id[site]
            detector = Detector.detector_id[detector]
        except KeyError:
            return None
            
        context = {
            'year' : int(year),
            'month' : int(month),
            'day' : int(day),
            'site' : site,
            'detector' : detector,
        }
        if rollback:
            context['rollback'] = {
                'year' : int(rollback_year),
                'month' : int(rollback_month),
                'day' : int(rollback_day),
            }
                    
        vld = DBI_get(self.select_related(), context)
        if vld:
            return vld.calibpmtspec_set
        else:
            return None
    
    
    def records(self, site, detector, task=0, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'calibpmtspec', site, detector, task, sim, character, width)
        return output
        

# =====================================
class CalibpmtspecManager(models.Manager):
    
    def trend(self, site, detector, ring, column, in_out=1, task=0, sim=1):
        '''Returns correct dbi values as a funtion of time'''
        try:
            if detector in ['AD1', 'AD2', 'AD3', 'AD4']:
                pmtid = SensorId.ADfullPackedData(
                    Site.site_id[site], 
                    Detector.detector_id[detector], 
                    ring, column)
            elif detector in ['IWS', 'OWS']:
                pmtid = SensorId.WPfullPackedData(
                    Site.site_id[site], 
                    Detector.detector_id[detector], 
                    ring, column, in_out) # wall = ring, spot = column
            else:
                return []
        except KeyError:
            return []
            
        
        dbi_records = DBI_trend(
            self.select_related().filter(
                pmtid=pmtid,
            ), site, detector, task, sim)
        
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
                'pmtdescrib' : value['record'].pmtdescrib,
                'pmtspehigh' : value['record'].pmtspehigh,
                'pmtspelow' : value['record'].pmtspelow,
                'pmttoffset' : value['record'].pmttoffset,
            })
            
        # from pprint import pprint
        # pprint(values)
        # pprint(uncovered_periods)
            
        return values

            
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
    
    objects = CalibpmtspecvldManager()
    
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
    
    objects = CalibpmtspecManager()
    
    class Meta:
        db_table = u'CalibPmtSpec'
        ordering = ['vld']

    def __unicode__(self):
        return self.pmtdescrib


# =====================================
class CalibpmtfinegainvldManager(models.Manager):
    '''Manager'''
    
    def pmtspecSet(self, site, detector, year, month, day,
        rollback=False, rollback_year='', rollback_month='', rollback_day=''):
        '''Returns a QuerySet of DBI Calibpmtspec'''
        try:
            site = Site.site_id[site]
            detector = Detector.detector_id[detector]
        except KeyError:
            return None
            
        context = {
            'year' : int(year),
            'month' : int(month),
            'day' : int(day),
            'site' : site,
            'detector' : detector,
        }
        if rollback:
            context['rollback'] = {
                'year' : int(rollback_year),
                'month' : int(rollback_month),
                'day' : int(rollback_day),
            }
                    
        vld = DBI_get(self.select_related(), context)
        if vld:
            return vld.calibpmtfinegain_set
        else:
            return None
    
    def records(self, site, detector, task=1, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'calibpmtfinegain', site, detector, task, sim, character, width)
        return output

# =====================================
class CalibpmtfinegainManager(models.Manager):
    
    def trend(self, site, detector, board, connector, task=0, sim=1):
        '''Returns correct dbi values as a funtion of time'''
        try:
            channelid = ChannelId.fullPackedData(
                Site.site_id[site], 
                Detector.detector_id[detector], 
                board, connector)
            # print channelid
        except KeyError:
            return []
            
        
        dbi_records = DBI_trend(
            self.select_related().filter(
                channelid=channelid,
            ), site, detector, task, sim)
        
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
                'spehigh' : value['record'].spehigh,
                'spehigherror' : value['record'].spehigherror,
                'sigmaspehigh' : value['record'].sigmaspehigh,
                'spehighfitqual' : value['record'].spehighfitqual,
            })
            
        # from pprint import pprint
        # pprint(values)
        # pprint(uncovered_periods)
            
        return values

# =====================================
class Calibpmtfinegainvld(models.Model):
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

    objects = CalibpmtfinegainvldManager()

    class Meta:
        db_table = u'CalibPmtFineGainVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, ) 

# =====================================
class Calibpmtfinegain(models.Model):
    vld = models.ForeignKey(Calibpmtfinegainvld, db_column='SEQNO') # Field name made lowercase.    
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Field name made lowercase.
    channelid = models.IntegerField(null=True, db_column='CHANNELID', blank=True) # Field name made lowercase.
    spehigh = models.FloatField(null=True, db_column='SPEHIGH', blank=True) # Field name made lowercase.
    spehigherror = models.FloatField(null=True, db_column='SPEHIGHERROR', blank=True) # Field name made lowercase.
    sigmaspehigh = models.FloatField(null=True, db_column='SIGMASPEHIGH', blank=True) # Field name made lowercase.
    spehighfitqual = models.FloatField(null=True, db_column='SPEHIGHFITQUAL', blank=True) # Field name made lowercase.
    
    objects = CalibpmtfinegainManager()
    
    class Meta:
        db_table = u'CalibPmtFineGain'
        ordering = ['vld']
    
    def __unicode__(self):
        return self.channelid    


# =====================================
class CalibpmttimingvldManager(models.Manager):
    '''Manager'''
    
    def records(self, site, detector, task=0, sim=1, character='|', width=50):
        '''Returns formated DBI records'''
        output = DBI_records(self, 'calibpmttiming', site, detector, task, sim, character, width)
        return output

# =====================================
class Calibpmttimingvld(models.Model):
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

    objects = CalibpmttimingvldManager()

    class Meta:
        db_table = u'CalibPmtTimingVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )
        
# =====================================
class Calibpmttiming(models.Model):
    vld = models.ForeignKey(Calibpmttimingvld, db_column='SEQNO') # Field name made lowercase.        
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Field name made lowercase.
    channelid = models.IntegerField(null=True, db_column='CHANNELID', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='STATUS', blank=True) # Field name made lowercase.
    par0 = models.FloatField(null=True, db_column='PAR0', blank=True) # Field name made lowercase.
    par1 = models.FloatField(null=True, db_column='PAR1', blank=True) # Field name made lowercase.
    par2 = models.FloatField(null=True, db_column='PAR2', blank=True) # Field name made lowercase.
    par3 = models.FloatField(null=True, db_column='PAR3', blank=True) # Field name made lowercase.
    par4 = models.FloatField(null=True, db_column='PAR4', blank=True) # Field name made lowercase.
    par5 = models.FloatField(null=True, db_column='PAR5', blank=True) # Field name made lowercase.
    fitqual = models.FloatField(null=True, db_column='FITQUAL', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'CalibPmtTiming'
        ordering = ['vld']
    
    def __unicode__(self):
        return self.channelid

# =====================================
class Cablemapvld(models.Model):
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
    
    objects = CablemapvldManager()
        
    class Meta:
        db_table = u'CableMapVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, ) 

# =====================================
class Cablemap(models.Model):
    vld = models.ForeignKey(Cablemapvld, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Fake pk, will duplicate (legacy db use multiple fields as pk)
    sensorid = models.IntegerField(null=True, db_column='SENSORID', blank=True) # Field name made lowercase.
    channelid = models.IntegerField(null=True, db_column='CHANNELID', blank=True) # Field name made lowercase.
    
    objects = CablemapManager()
        
    class Meta:
        db_table = u'CableMap'

    def __unicode__(self):
        return u'channelid: %d' % self.channelid

    def site(self):
        return (self.channelid & 0xff000000) >> 24

    def detector(self):
        return (self.channelid & 0x00ff0000) >> 16
        
    def board(self):
        return '%02d' % ((self.channelid & 0x0000ff00) >> 8, )

    def connector(self):
        return '%02d' % (self.channelid & 0x000000ff, )

    def ring(self):
        if self.detector() in [1, 2, 3, 4]:
            return '%02d' % ((self.sensorid & 0x0000ff00) >> 8, )
        else:
            return ''

    def column(self):
        if self.detector() in [1, 2, 3, 4]:
            return '%02d' % (self.sensorid & 0x000000ff, )
        else:
            return ''   

    def wall(self):
        if self.detector() in [5, 6]:
            return '%02d' % ((self.sensorid & 0x00000f00) >> 8, )
        else:
            return ''

    def spot(self):
        if self.detector() in [5, 6]:
            return '%02d' % (self.sensorid & 0x000000ff, )
        else:
            return ''

    def in_out(self):
        if self.detector() in [5, 6]:
            if ((self.sensorid & 0x0000f000)):
                return 'in'
            else:
                return 'out'
        else:
            return ''
    
    def feechanneldesc(self):
        return '%s%s-board%s-connector%s' % (
            Site.id_site.get(self.site(), ''),
            Detector.id_detector.get(self.detector(), ''),
            self.board(), self.connector(),
        )

    def sensordesc(self):
        if not self.ring() == '':
            return '%s%s-ring%s-column%s' % (
                Site.id_site.get(self.site(), ''),
                Detector.id_detector.get(self.detector(), ''),
                self.ring(), self.column(),
            )
        else:
            return '%s%s-wall%s-spot%s' % (
                Site.id_site.get(self.site(), ''),
                Detector.id_detector.get(self.detector(), ''),
                self.wall(), self.spot(),
            )                           
                     
    def unpack(self):
        return {
            'site' : self.site(),
            'detector' : self.detector(),
            'board' : self.board(),
            'connector' : self.connector(),
            'ring' : self.ring(),
            'column' : self.column(),
            'wall' : self.wall(),
            'spot' : self.spot(),
            'in_out' : self.in_out(),
        }
        