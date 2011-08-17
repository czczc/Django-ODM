# DYB PMT ID conventions

# ==============================================
class ChannelId(object):
    '''Channelid convention'''
    
    @classmethod
    def fullPackedData(cls, site, detector, board, connector):
        return (0x000000ff & connector) | (0x000000ff & board)<<8 | (0x000000ff & detector)<<16 | (0x000000ff & site)<<24
            
    def __init__(self, channelid):
        self.channelid = channelid
        
    def site(self):
        return (self.channelid & 0xff000000) >> 24

    def detector(self):
        return (self.channelid & 0x00ff0000) >> 16
        
    def board(self):
        return '%02d' % ((self.channelid & 0x0000ff00) >> 8, )

    def connector(self):
        return '%02d' % (self.channelid & 0x000000ff, )
        

# ==============================================
class SensorId(object):
    '''Sensorid convention'''

    @classmethod
    def ADfullPackedData(cls, site, detector, ring, column):
        if detector in [1, 2, 3, 4]:
            return (0x000000ff & column) | (0x000000ff & ring)<<8 | (0x000000ff & detector)<<16 | (0x000000ff & site)<<24
        else:
            return None
            
    @classmethod
    def WPfullPackedData(cls, site, detector, wall, spot, in_out):
        if detector in [5, 6]:
            return (0x000000ff & spot) | (0x0000000f & wall)<<8 | (0x0000000f & in_out)<<12 | (0x000000ff & detector)<<16 | (0x000000ff & site)<<24
        else:
            return None
                        
    def __init__(self, sensorid):
        self.sensorid = sensorid

    def site(self):
        return (self.sensorid & 0xff000000) >> 24

    def detector(self):
        return (self.sensorid & 0x00ff0000) >> 16
        
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
            