# conventions

class DaqTriggerType(object):
    '''Trigger definition in LTB manual doc-3443'''
    trigger_definition = {
         'Unknown'   : 0,
         'Manual'    : 1,
         'External'  : 2,
         'Periodic'  : 4,
         'Pedestal'  : 8,
         'Calib'     : 16,
         'Random'    : 32,
         'Reserved1'  : 64,
         'Reserved2'  : 128,
         'NHit'      : 256,
         'Esum_ADC'  : 512,
         'Esum_High' : 1024,
         'Esum_Low'  : 2048,
         'Esum'      : 4096,
    }
    
    def __init__(self, trigger_code):
        self.trigger_code = int(trigger_code);
        self._decode()
        
    def _decode(self):
        for trigger, bit in self.trigger_definition.items():
            if self.trigger_code & bit:
                self.__setattr__(trigger, True)
                
    def __str__(self):
        string = ''
        for trigger in sorted(self.trigger_definition):
            if trigger in self.__dict__:
                string = string + trigger + ' | '
        if string:
            return string[:-3]
            