# Managing simulation diagnositcs info
from odm.production.diagnostics import Diagnostics
import os

class Simulation(Diagnostics):
    '''class to manage simulation diagnositcs info '''
    
    local_base_dir = '/project/projectdirs/dayabay/www/dybprodSim'
    xml_base_url = 'http://portal.nersc.gov/project/dayabay/dybprodSim/'
    
    def __init__(self, runno=''):
        super(Simulation, self).__init__(runno)
        self.base_url = 'http://portal.nersc.gov/project/dayabay/dybprodSim/'
        self.info.update({
            'Sources' : {
                'Muon' : [
                    # {
                    #     'figname' : '',
                    #     'figpath' : '',
                    # },
                ],
            },
        })
    
    def _load_info(self):
        super(Simulation, self)._load_info()
        dirname = os.path.dirname(self.info['run_xml'])
        fig_dict = {
            'Muon' : [
                'ClosestL',
                'DeltaT',
                'E',
                'EdepositVSTrkLeninAD',
                'EdepositVSTrkLeninWS',
                'LogDeltaT',
                'NSpallationN',
                'Phi',
                'QuenchVSdepositEinLS',
                'TNCapture',
                'Theta',
                'VtxyVSx',
                'VtxzVSx',
                'VtxzVSy',
                'simhitsVSTrkLeninAD',
                'simhitsVSTrkLeninWS',
                'yVSxNCapture',
                'zVSxNCapture',
                'zVSyNCapture',
            ],
            'Rad' : [
                'AllKinE',
                'AlphaKinE',
                'BetaKinE',
                'DeltaT',
                'GammaKinE',
                'LogDeltaT',
                'VtxyVSx',
                'VtxzVSx',
                'VtxzVSy',
                'quenVSdepo',
                'simhitsVSdepo',
            ],
            'IBD' : [
                'DeltaT',
                'Eanue',
                'KEN',
                'KEP',
                'LogDeltaT',
                'NCapZ',
                'PhiNu',
                'TNAbsorption',
                'TNCaptureinC',
                'TNCaptureinGd',
                'TNCaptureinH',
                'TNCaptureinOthers',
                'ThetaN',
                'ThetaNu',
                'ThetaP',
                'VtxyVSx',
                'VtxzVSx',
                'VtxzVSy',
                'quenVSdepo',
                'simhitsVSquen',
                'yVSxNAbsorption',
                'yVSxNCaptureinC',
                'yVSxNCaptureinGd',
                'yVSxNCaptureinH',
                'yVSxNCaptureinOthers',
                'zVSxNAbsorption',
                'zVSxNCaptureinC',
                'zVSxNCaptureinGd',
                'zVSxNCaptureinH',
                'zVSxNCaptureinOthers',
                'zVSyNAbsorption',
                'zVSyNCaptureinC',
                'zVSyNCaptureinGd',
                'zVSyNCaptureinH',
                'zVSyNCaptureinOthers',
            ],
        }
        for figname in fig_dict['Muon']:
            name = 'Muon'
            self.info['Sources'].setdefault(name ,[]).append({
                'figname' : figname + '(' + name + ')',
                'figpath' : dirname + '/mctruth/source_' + name.lower() + '/mc_' + figname + '_MUON.png'
            })            
        for figname in fig_dict['Rad']:
            for name in ['U238', 'Th232', 'K40', 'Co60']:
                self.info['Sources'].setdefault(name, []).append({
                    'figname' : figname + '(' + name + ')',
                    'figpath' : dirname + '/mctruth/source_' + name.lower() + '/mc_' + figname + '_RAD.png'
                }) 
        for figname in fig_dict['IBD']:
            name = 'IBD'
            self.info['Sources'].setdefault(name ,[]).append({
                'figname' : figname + '(' + name + ')',
                'figpath' : dirname + '/mctruth/source_' + name.lower() + '/mc_' + figname + '_IBD.png'
            })             
            