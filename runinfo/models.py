from django.db import models
from django.db.models import Q, F
from django.conf import settings

from odm.conventions.conf import Calibration, Detector, Site

from datetime import datetime, timedelta

class RuninfoManager(models.Manager):
    def list_runtype(self, runtype):
        '''list by run type'''
        if runtype == 'All':
            return self.select_related()
        return self.select_related().filter(runtype=runtype)
        
    def list_latest(self, days):
        '''list latest runs'''
        latest = datetime.utcnow() - timedelta(days=int(days))
        return self.select_related().filter(vld__timestart__gte=latest)
    
    def json_listall(self):
        '''format json type runinfo'''
        info = {
            # '<runno>' : {
            #     'runtype' : 'Physics',
            #     'partition' : 'EH1-SAB',
            # }
        }
        for run in self.all():
            runinfo = info.setdefault(run.runno, {})
            runinfo['runtype'] = run.runtype
        
        return info


class CalibruninfoManager(models.Manager):
    def list_sourcetype(self, sourcetype):
        '''list by source type'''
        if sourcetype == 'Ge68':
            return self.select_related().filter(
                  Q(sourceida=3, homea=0, lednumber1=0, lednumber2=0)
                | Q(sourceidb=3, homeb=0, lednumber1=0, lednumber2=0)
                | Q(sourceidc=3, homec=0, lednumber1=0, lednumber2=0))
        elif sourcetype == 'AmC_Co60':
            return self.select_related().filter(
                  Q(sourceida=2, homea=0, lednumber1=0, lednumber2=0)
                | Q(sourceidb=2, homeb=0, lednumber1=0, lednumber2=0)
                | Q(sourceidc=2, homec=0, lednumber1=0, lednumber2=0))
        elif sourcetype == 'MO_LED':
            return self.select_related().filter(
                  Q(lednumber1__gt=3))
        elif sourcetype == 'ACU_LED':
            return self.select_related().filter(
                  Q(homea=0, lednumber1=1)
                | Q(homeb=0, lednumber1=2)
                | Q(homec=0, lednumber1=3)) 
        elif sourcetype == 'Double_Pulse':
            return self.select_related().filter(
                ( Q(homea=0, lednumber1=1)
                | Q(homeb=0, lednumber1=2)
                | Q(homec=0, lednumber1=3) ) &
                ( Q(homea=0, lednumber2=1)
                | Q(homeb=0, lednumber2=2)
                | Q(homec=0, lednumber2=3) ) &
                ( ~Q(lednumber1=F('lednumber2')))
            ) 
        else:
           return self.none()
                    
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
        return self.timestart + timedelta(seconds=8*3600)   

    def timeend_beijing(self):
        return self.timeend + timedelta(seconds=8*3600)

#=====================================
class Daqruninfo(models.Model):
    vld = models.ForeignKey(Daqruninfovld, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # Fake pk
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

    def partition(self):
        '''return site string'''
        # temporary: return site-detector until multiple-detector scheme is set
        return ''.join(self.partitionname.split('_')[1:]).upper();     
    
    def site(self):
        return self.partition().split('-')[0]
        
    def detectors(self):
        site_det = self.partition().split('-')
        site = site_det[0]
        try:
            detector = site_det[1]
            if detector in Detector.detector_groups:
                return Detector.detector_groups[detector]
            else:
                return [ detector ]  # single detector
        except IndexError:
            return Detector.hall_detectors.get(site, [])

    def summary(self):
        html  = '<div class="grid_14" style="margin-top:10px;"><table>\n'
        html += '<thead><tr><th colspan="2" style="text-align: center;">General Run infomation</th></tr></thead><tbody>\n'
        html += "<tr><td class='descr'>Run Number</td><td class='value'>%d</td></tr>\n" % self.runno
        html += "<tr><td class='descr'>Run Type</td><td class='value'>%s</td></tr>\n" % self.runtype
        html += "<tr><td class='descr'>Start Time [Beijing]</td><td class='value'>%s</td></tr>\n" % self.vld.timestart_beijing()
        html += "<tr><td class='descr'>Stop Time [Beijing]</td><td class='value'>%s</td></tr>\n" % self.vld.timeend_beijing()
        html += "<tr><td class='descr'>Partition</td><td class='value'>%s</td></tr>\n" % self.partition()
        html += "<tr><td class='descr'>Schema-Base-Data Ver.</td><td class='value'>%d-%d-%d</td></tr>\n" % (self.schemaversion, self.baseversion, self.dataversion)
        html += "</tbody></table></div>"
        return html
        

# =====================================
class Daqcalibruninfovld(models.Model):
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
        db_table = u'DaqCalibRunInfoVld'
        ordering = ['-seqno']

    def __unicode__(self):
        return u'seq %d' % (self.seqno, )

    def runlength(self):
        return self.timeend - self.timestart

    def timestart_beijing(self):
        return self.timestart + timedelta(seconds=8*3600)   

# =====================================
class Daqcalibruninfo(models.Model):
    vld = models.ForeignKey(Daqcalibruninfovld, db_column='SEQNO') # Field name made lowercase.
    # seqno = models.IntegerField(primary_key=True, db_column='SEQNO') # Field name made lowercase.
    row_counter = models.IntegerField(primary_key=True, db_column='ROW_COUNTER') # # Fake pk
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
    
    # a/b/c refers to either ACU A/B/C or MO LED A/B/C
    has_a = has_b = has_c = False
    is_led_run = False
    source_type_a = source_type_b = source_type_c = ''
    location_a = location_b = location_c = ''
    
    objects = CalibruninfoManager()
    
    class Meta:
        db_table = u'DaqCalibRunInfo'
        ordering = ['-runno']
    
    def __unicode__(self):
        return u'calib run %d' % (self.runno, )

    def get_absolute_url(self):
        return "%s/run/%i/" % (settings.SITE_ROOT, self.runno)
    
    def detector(self):
        return Site.daq_detectors.get(self.detectorid, 'Unknown')    
    
    def acu_for_source(self):
        acu_list = []
        if (self.homea==0 and self.sourceida in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            acu_list.append('A')
        if (self.homeb==0 and self.sourceidb in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            acu_list.append('B')
        if (self.homec==0 and self.sourceidc in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            acu_list.append('C')
        return ', '.join(acu_list)

                
    def z_for_source(self):
        z_list = []
        if (self.homea==0 and self.sourceida in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            z_list.append(str(self.zpositiona))
        if (self.homeb==0 and self.sourceidb in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            z_list.append(str(self.zpositionb))
        if (self.homec==0 and self.sourceidc in [2,3] 
            and self.lednumber1==0 and self.lednumber2==0):
            z_list.append(str(self.zpositionc))
        return ', '.join(z_list)        

                
    def mo_led(self):
        if self.lednumber1 in [4,5,6]:
            return Calibration.mo_led_location[self.lednumber1]
        else:
            return ''


    def acu_for_led(self):
        if (self.homea==0 and self.lednumber1==1):
            return 'A'
        if (self.homeb==0 and self.lednumber1==2):
            return 'B'
        if (self.homec==0 and self.lednumber1==3):
            return 'C'
        return ''
        
    def z_for_led(self):
        if (self.homea==0 and self.lednumber1==1):
            return self.zpositiona
        if (self.homeb==0 and self.lednumber1==2):
            return self.zpositionb
        if (self.homec==0 and self.lednumber1==3):
            return self.zpositionc
        return ''    

    def acu2_for_led(self):
        if (self.homea==0 and self.lednumber2==1 and not self.lednumber1==self.lednumber2):
            return 'A'
        if (self.homeb==0 and self.lednumber2==2 and not self.lednumber1==self.lednumber2):
            return 'B'
        if (self.homec==0 and self.lednumber2==3 and not self.lednumber1==self.lednumber2):
            return 'C'
        return ''

    def z2_for_led(self):
        if (self.homea==0 and self.lednumber2==1 and not self.lednumber1==self.lednumber2):
            return self.zpositiona
        if (self.homeb==0 and self.lednumber2==2 and not self.lednumber1==self.lednumber2):
            return self.zpositionb
        if (self.homec==0 and self.lednumber2==3 and not self.lednumber1==self.lednumber2):
            return self.zpositionc
        return ''
                            
    def humanize(self):
        self._humanize_led()
        self._humanize_a()
        self._humanize_b()
        self._humanize_c()

    def _humanize_led(self):
        if self.lednumber1 or self.lednumber2:
            # It's an LED run
            self.is_led_run = True
            
            if self.lednumber1:
                self.has_a = True
                self.source_type_a = Calibration.led_type[self.lednumber1]
                self.location_a = Calibration.location[self.lednumber1]
            
            if self.lednumber2:
                self.has_b = True
                self.source_type_b = Calibration.led_type[self.lednumber2]
                self.location_b = Calibration.location[self.lednumber2]
            
    def _humanize_a(self):
        if self.is_led_run: return
        if self.sourceida:
            source_type = Calibration.source_type.get(self.sourceida, '')
            if not source_type == 'LED':
                self.has_a = True
                self.source_type_a = source_type
                self.location_a = Calibration.location[1]

    def _humanize_b(self):
        if self.is_led_run: return
        if self.sourceidb:
            source_type = Calibration.source_type.get(self.sourceidb, '')
            if not source_type == 'LED':
                self.has_b = True
                self.source_type_b = source_type
                self.location_b = Calibration.location[2]

    def _humanize_c(self):
        if self.is_led_run: return
        if self.sourceidc:
            source_type = Calibration.source_type.get(self.sourceidc, '')
            if not source_type == 'LED':
                self.has_c = True
                self.source_type_c = source_type
                self.location_c = Calibration.location[3]
    
            