from django.db import models
from odm.runinfo.models import Daqruninfo
from odm.conventions.conf import DaqTriggerType

import re

class RunconfigManager(models.Manager):
    '''
    The legacy Runconfig table doesn't fit to django model well.
    Use raw query. -CZ
    '''
    runno = ''
    info = {
        'runno' : '',
        'runtype' : '',
        'detectors' : {
            # 'SAB-AD2' : {
            #     'FADCName' : '',
            #     'LTBName' : '',
            #     'FEEName' : '',
            #     'FEEBoards' : [],
            #     'LTBfirmwareVersion' : '',
            #     'FEEBoardVersion' : '',
            #     'FEECPLDVersion' : '',
            #     'FEEBaseline_enable' : '',
            #     'FEEWaveform_enable' : '',
            #     'FEEPrefix' : '',
            #     'DACSelect_UniformVal' : ''
            # },
            # 'SABAD1' : {},
        },
    }
    
    
    def fetch_all(self):
        self.info['runno'] = self.runno
        # self.info[self.runno] = 'there'
        for version in ['base', 'data']:
            self.fetch_active_detectors(version)
        
        for detector in self.info['detectors']:
            for version in ['base', 'data']:
                self.fetch_detector_settings(version, detector)
                LTBName = self.info['detectors'][detector].get('LTBName', '')
                if LTBName:
                    self.fetch_LTB_settings(version, detector, LTBName)
                FEEPrefix = self.info['detectors'][detector].get('FEEPrefix', '')
                if FEEPrefix:
                    self.fetch_FEE_settings(version, detector, FEEPrefix)
        self.finalize()
    
    
    def fetch_active_detectors(self, version):
        '''fetch active detectors'''
        
        # I intended to not use the .raw(queryString, param) syntax
        # to avoid the escape of variable name
        queryString = '''
            SELECT *
            FROM DaqRunConfig JOIN DaqRunInfo 
            ON DaqRunInfo.schemaVersion=DaqRunConfig.schemaVersion 
            AND DaqRunInfo.%sVersion=DaqRunConfig.dataVersion
            AND DaqRunConfig.className='ROSConfiguration'
            AND DaqRunConfig.name='childObjectId_Detectors'
            AND DaqRunInfo.runNo='%s'
        ''' % (version, self.runno)
        rawQuerySet = list(self.raw(queryString))
        
        if version == 'base':
            self.info['detectors'] = {}    # clear detector data for any base version
        elif len(rawQuerySet):    
            self.info['detectors'] = {}    # clear detector data if data version exists
            
        for daq in rawQuerySet:
            self.info['detectors'][daq.stringvalue] = {}
            self.info['runtype'] = daq.runType
            # self.info[version] = daq.stringvalue


    def fetch_detector_settings(self, version, detector):
        '''fetch detector settings'''

        queryString = '''
            SELECT *
            FROM DaqRunConfig JOIN DaqRunInfo 
            ON DaqRunInfo.schemaVersion=DaqRunConfig.schemaVersion 
            AND DaqRunInfo.%sVersion=DaqRunConfig.dataVersion
            AND DaqRunConfig.objectID='%s'
            AND DaqRunInfo.runNo='%s'
        ''' % (version, detector, self.runno)
        rawQuerySet = list(self.raw(queryString))
        
        for daq in rawQuerySet:
            detinfo = self.info['detectors'][detector]

            FADCName = daq.stringFromName('childObjectId_FADC') 
            if (FADCName): detinfo['FADCName'] = FADCName
            
            LTBName = daq.stringFromName('childObjectId_LTB')
            if (LTBName): detinfo['LTBName'] = LTBName
            
            LTBfirmwareVersion = daq.intFromName('LTBfirmwareVersion') 
            if (LTBfirmwareVersion): detinfo['LTBfirmwareVersion'] = LTBfirmwareVersion

            FEEBoardVersion = daq.intFromName('FEEBoardVersion') 
            if (FEEBoardVersion): detinfo['FEEBoardVersion'] = FEEBoardVersion
            
            FEECPLDVersion = daq.intFromName('FEECPLDVersion') 
            if (FEECPLDVersion): detinfo['FEECPLDVersion'] = FEECPLDVersion
            
            FEEBaseline_enable = daq.stringFromName('FEEBaseline_enable') 
            if (FEEBaseline_enable): detinfo['FEEBaseline_enable'] = FEEBaseline_enable
            
            FEEWaveform_enable = daq.stringFromName('FEEWaveform_enable') 
            if (FEEWaveform_enable): detinfo['FEEWaveform_enable'] = FEEWaveform_enable
            
            FEE = daq.stringFromName('childObjectId_Modules')
            if (FEE): 
                detinfo.setdefault('FEEBoards', []).append(FEE)
                if not detinfo.get('FEEPrefix', ''):
                    detinfo['FEEPrefix'] = re.search(r'FEE_(.+)_', FEE).group(1)


    def fetch_LTB_settings(self, version, detector, LTBName):
        '''fetch LTB settings'''
        
        # to comply to a strange setting for SAB-AD1
        if (LTBName == 'LTB_0'): LTBName = ''
        else: LTBName = LTBName + '_'
        
        queryString = '''
            SELECT *
            FROM DaqRunConfig JOIN DaqRunInfo 
            ON DaqRunInfo.schemaVersion=DaqRunConfig.schemaVersion 
            AND DaqRunInfo.%sVersion=DaqRunConfig.dataVersion
            AND DaqRunConfig.objectID='%s'
            AND DaqRunInfo.runNo='%s'
        ''' % (version, LTBName+self.info['runtype']+'Mode', self.runno)
        rawQuerySet = list(self.raw(queryString))

        for daq in rawQuerySet:
            detinfo = self.info['detectors'][detector]

            # ESum
            DAC_total_value = daq.intFromName('DAC_total_value') 
            if (DAC_total_value): detinfo['DAC_total_value'] = DAC_total_value

            # NHit
            HSUM_trigger_threshold = daq.intFromName('HSUM_trigger_threshold') 
            if (HSUM_trigger_threshold): detinfo['HSUM_trigger_threshold'] = HSUM_trigger_threshold

            # Trigger type
            LTB_triggerSource = daq.intFromName('LTB_triggerSource') 
            if (LTB_triggerSource):
                detinfo['LTB_triggerSource'] = LTB_triggerSource
                detinfo['LTB_triggerType'] = str(DaqTriggerType(LTB_triggerSource))


    def fetch_FEE_settings(self, version, detector, FEEPrefix):
        '''fetch LTB settings'''
        
        queryString = '''
            SELECT *
            FROM DaqRunConfig JOIN DaqRunInfo 
            ON DaqRunInfo.schemaVersion=DaqRunConfig.schemaVersion 
            AND DaqRunInfo.%sVersion=DaqRunConfig.dataVersion
            AND DaqRunConfig.name='DACSelect'
            AND DaqRunConfig.objectID LIKE '%s%%%%'
            AND DaqRunConfig.stringValue='UniformVal'
            AND DaqRunInfo.runNo='%s'
        ''' % (version, self.info['runtype']+'Threshold_'+FEEPrefix, self.runno)
        rawQuerySet = list(self.raw(queryString))

        for daq in rawQuerySet:
            detinfo = self.info['detectors'][detector]
            
            #DACSelect UniformVal suedo FEE Channel
            DACSelect_UniformVal = daq.objectid
            if (DACSelect_UniformVal): detinfo['DACSelect_UniformVal'] = DACSelect_UniformVal
        
        DACSelect_UniformVal = self.info['detectors'][detector].get('DACSelect_UniformVal','')
        if DACSelect_UniformVal:
            queryString = '''
                SELECT *
                FROM DaqRunConfig JOIN DaqRunInfo 
                ON DaqRunInfo.schemaVersion=DaqRunConfig.schemaVersion 
                AND DaqRunInfo.%sVersion=DaqRunConfig.dataVersion
                AND DaqRunConfig.name='DACUniformVal'
                AND DaqRunConfig.objectID='%s'
                AND DaqRunInfo.runNo='%s'
            ''' % (version, DACSelect_UniformVal, self.runno)
            rawQuerySet = list(self.raw(queryString))
            for daq in rawQuerySet:
                detinfo = self.info['detectors'][detector]
    
                #DACSelect UniformVal suedo FEE Channel
                DACUniformVal = daq.intvalue
                if (DACUniformVal): 
                    detinfo['DACUniformVal'] = str(DACUniformVal)
                elif (DACUniformVal == 0):
                    detinfo['DACUniformVal'] = '0'

    
    def finalize(self):
        pass
            


# =====================================
class Daqrunconfig(models.Model):
    schemaversion = models.IntegerField(primary_key=True, db_column='schemaVersion') # Field name made lowercase.
    dataversion = models.IntegerField(db_column='dataVersion') # Field name made lowercase.
    creationversion = models.IntegerField(null=True, db_column='creationVersion', blank=True) # Field name made lowercase.
    classname = models.CharField(max_length=192, db_column='className') # Field name made lowercase.
    objectid = models.CharField(max_length=192, db_column='objectId') # Field name made lowercase.
    name = models.CharField(max_length=384)
    parentposition = models.IntegerField(db_column='parentPosition') # Field name made lowercase.
    intvalue = models.BigIntegerField(null=True, db_column='intValue', blank=True) # Field name made lowercase.
    floatvalue = models.FloatField(null=True, db_column='floatValue', blank=True) # Field name made lowercase.
    stringvalue = models.CharField(max_length=192, db_column='stringValue', blank=True) # Field name made lowercase.
    
    objects = RunconfigManager()
    
    class Meta:
        db_table = u'DaqRunConfig'
        ordering = ['-schemaversion', '-dataversion']
    
    def __unicode__(self):
        return u'%d-%d' % (self.schemaversion, self.dataversion)
        
    def stringFromName(self, name):
        if (self.name == name):
            return self.stringvalue
        else:
            return ''

    def intFromName(self, name):
        if (self.name == name):
            return str(self.intvalue)
        else:
            return ''    
            
    def stringFromObjectID(self, objectid):
        if (self.objectid == objectid):
            return self.stringvalue
        else:
            return ''

    def intFromObjectID(self, objectid):
        if (self.objectid == objectid):
            return str(self.intvalue)
        else:
            return ''             
    
