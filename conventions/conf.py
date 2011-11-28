# some DYB conventions

# ==============================================
class Site(object):
    '''Site convention'''
    
    site_id = {
        'Unknown'      : 0, 
        'DayaBay'      : 1,
        'LingAo'       : 2,
        'Far'          : 4,
        'Mid'          : 8,
        'Aberdeen'     : 16,
        'SAB'          : 32,
        'PMTBenchTest' : 64,
    }

    id_site = {
        0  : 'Unknown',     
        1  : 'DayaBay',       
        2  : 'LingAo',        
        4  : 'Far',           
        8  : 'Mid',           
        16 : 'Aberdeen',      
        32 : 'SAB',           
        64 : 'PMTBenchTest',  
    }

    site_alias = {
        'DayaBay' : 'EH1',
        'LingAo'  : 'EH2',
        'Far'     : 'EH3',
        'SAB'     : 'SAB',
    }


    daq_id = {
        'SAB-AD1' : 97,
        'SAB-AD2' : 98,
        'EH1-AD1' : 17,
        'EH1-AD2' : 18,
        'EH2-AD1' : 33,
        'EH3-AD1' : 49,
        'EH3-AD2' : 50,
        'EH3-AD3' : 51,
    }
    
    daq_detectors=dict([(v,k) for (k,v) in daq_id.items()])
    
    # daq_detectors = {
    #     97 : 'SAB-AD1',
    #     98 : 'SAB-AD2',
    # }
    
# ==============================================
class Detector(object):
    '''Detetor convention'''
    
    detector_id = {
        'All' : 0,
        'AD1' : 1,
        'AD2' : 2,
        'AD3' : 3,
        'AD4' : 4,
        'IWS' : 5,
        'OWS' : 6,
        'RPC' : 7,
    }
    
    id_detector = {
        0 : 'All',
        1 : 'AD1',
        2 : 'AD2',
        3 : 'AD3',
        4 : 'AD4',
        5 : 'IWS',
        6 : 'OWS',
        7 : 'RPC',
    }
    
    detector_alias = {
        'AD1' : 'AD1',
        'AD2' : 'AD2',
        'AD3' : 'AD3',
        'AD4' : 'AD4',
        'IWS' : 'WPI',
        'OWS' : 'WPO',
        'RPC' : 'RPC',
    }
    
    hall_detectors = {
        'EH1' : ['AD1', 'AD2', 'WPI', 'WPO', 'RPC'],
        'EH2' : ['AD1', 'AD2', 'WPI', 'WPO', 'RPC'],
        'EH3' : ['AD1', 'AD2', 'AD3', 'AD4', 'WPI', 'WPO', 'RPC'],
    }
    
    detector_groups = {
        'AD' : ['AD1', 'AD2', 'AD3', 'AD4'],
        'WP' : ['WPI', 'WPO'],
    }


# ==============================================
class DaqTriggerType(object):
    '''Trigger definition in LTB manual doc-3443'''
    trigger_type = {
         'Unknown'   : 0,
         'Manual'    : 1,
         'Cross'     : 2,
         'Periodic'  : 4,
         'Pedestal'  : 8,
         'Calib'     : 16,
         'Random'    : 32,
         'Reserved1' : 64,
         'Reserved2' : 128,
         'NHit'      : 256,
         'Esum_ADC'  : 512,
         'Esum_High' : 1024,
         'Esum_Low'  : 2048,
         'Esum'      : 4096,
         'NHIT_LOW'  : 8192,
         'NHIT_High' : 16384,
    }
    
    def __init__(self, trigger_code):
        self.trigger_code = int(trigger_code)
        self._decode()
        
    def _decode(self):
        for trigger, bit in self.trigger_type.items():
            if self.trigger_code & bit:
                self.__setattr__(trigger, True)
                
    def __str__(self):
        string = ''
        for trigger in sorted(self.trigger_type):
            if trigger in self.__dict__:
                string = string + trigger + ' | '
        if string:
            return string[:-3]


# ==============================================
class Calibration(object):
    '''Calibration convention'''
    
    source_type = {
        # for ACU only
        0 : 'Unknown',
        1 : 'LED',
        2 : 'AmC_Co60',
        3 : 'Ge68',
    }
    
    led_type = {
        0 : 'Unknown',
        1 : 'LED',
        2 : 'LED',
        3 : 'LED',
        4 : 'MO_LED',
        5 : 'MO_LED',
        6 : 'MO_LED',
    }
    
    location = {
        0 : 'Unknown',
        1 : 'ACU_A (Central Axis)',
        2 : 'ACU_B (GdLS Edge)',
        3 : 'ACU_C (Gamma Catcher)',
        # LED only
        4 : 'AD_Wall_Lower',
        5 : 'AD_Wall_Center',
        6 : 'AD_Wall_Upper',
    }
    
    mo_led_location = {
        4 : 'Lower',
        5 : 'Center',
        6 : 'Upper',
    }
    