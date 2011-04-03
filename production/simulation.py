# Managing simulation diagnositcs info
from odm.production.diagnostics import Diagnostics

class Simulation(Diagnostics):
    '''class to manage simulation diagnositcs info '''
    
    xml_base_url = 'http://portal.nersc.gov/project/dayabay/dybprodSim/'
    runs_xml = 'http://portal.nersc.gov/project/dayabay/dybprodSim/runs.xml'
    
    def __init__(self, runno=''):
        super(Simulation, self).__init__(runno)
        self.base_url = 'http://portal.nersc.gov/project/dayabay/dybprodSim/'
