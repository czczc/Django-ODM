from django.db import models
from odm.conventions.util import DBI_get, DBI_format
from odm.conventions.conf import Site, Detector


# =====================================
class CableMapVldManager(models.Manager):
    
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


# =====================================
class FeeCableMapManager(models.Manager):
    
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
            return vld.feecablemap_set
        else:
            return None

# =====================================
class CalibPMTSpecManager(models.Manager):
    
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
    
    
    def pmtspecTrend(self, site, detector, pmtid, format='txt'):
        '''Returns DBI values'''
        try:
            site = Site.site_id[site]
            detector = Detector.detector_id[detector]
        except KeyError:
            return None
        
        values = self.select_related().filter(
            subsite=detector,
            simmask=1,
            sitemask=site
        ).filter(calibpmtspec__pmtid=pmtid
        ).values('seqno', 'timestart', 'timeend', 'insertdate',
            'calibpmtspec__pmtspehigh',
            'calibpmtspec__pmtspelow',
            'calibpmtspec__pmttoffset',
        )
        
        output = DBI_format(values, format)
        
        return

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
    
    def unpack(self):
        sitedet, board, connector = self.feechanneldesc.split('-')
        board = board.replace('board', '')
        connector = connector.replace('connector', '')
        
        try:
            sitedet, ring, column, in_out = self.sensordesc.split('-')
        except ValueError:
            sitedet, ring, column = self.sensordesc.split('-')
            in_out = ''
        
        ring = ring.replace('ring', '')
        column = column.replace('column', '')
        wall = spot = ''
        
        try:
            int(ring)
        except ValueError:
            wall = ring.replace('wall', '')
            spot = column.replace('spot', '')
            ring = column = ''
             
        return {
            'board' : board,
            'connector' : connector,
            'ring' : ring,
            'column' : column,
            'wall' : wall,
            'spot' : spot,
            'in_out' : in_out,
        }

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
    
    objects = CableMapVldManager()
        
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
        