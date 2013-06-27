# Managing diagnositcs info 
import urllib2
from xml.etree import cElementTree as ElementTree
from django.conf import settings
import os
 
class Diagnostics(object):
    '''class to manage diagnositcs info '''
    
    local_base_dir = '/project/projectdirs/dayabay/www/dybprod'
    xml_base_url = 'https://portal.nersc.gov/project/dayabay/dybprod/'
    runs_xml = 'runs.xml'
    
    def __init__(self, runno=''):
        self.runno = runno
        
        # base_url can be different from xml_base_url on a run-by-run basis
        # so that they can be served on diffrent servers.
        # after fixing inodes issue, all can be served on NERCS now
        if settings.SITE_IHEP:
            pass
            self.base_url = 'http://202.122.37.74/odmfile/'
            self.local_base_dir = '/data/odm'
            self.xml_base_url = 'http://202.122.37.74/odmfile/'
        else:
            self.base_url = 'http://portal.nersc.gov/project/dayabay/dybprod/'            
 	    
        self.run_index = {}    # {runno: xml}
        self.run_list  = {}    # {runno: 1} 
        
        # info dictionary intended for json serializer
        self.info = {
            'base_url' : '',
            'xml_base_url' : '',
            'run_xml' : '',
            'detectors' : {
                # 'SABAD2' : [
                #     {
                #         'figname' : '',
                #         'figpath' : '',
                #     },
                # ],
                # 'SABAD1' : [],
            },
            'channels' : {
                # 'SABAD2' : {
                #     '06_01' : '1',
                #     '06_01' : '1',
                # },
                # 'SABAD1' : {},
            }
        }
    
    def fetch_all(self):
        # move this function out of __init__() to allow customized
        # child class behavior, e.g. the Simulation class 
        self._load_index()
        if (self.runno):
            self._load_info()
        
        # fh = open(os.path.join(self.local_base_dir, self.runs_xml))
        # tree = ElementTree.parse(fh)
        # return tree            
        # 
        # runs = tree.findall('run/runnumber')
        # for i, run in enumerate(runs):
            # self.run_index[run.text] = run_xmls[i].text
            # self.run_list[run.text] = '1'
        # run_xmls = tree.findall('run/runindex')    
        # self.run_list['1000'] = '1'
        
    def _load_index(self):
        '''load diagnostics run list'''
        try:
            fh = open(os.path.join(self.local_base_dir, self.runs_xml))
        except IOError:
            try:
                fh = urllib2.urlopen(self.xml_base_url + self.runs_xml)
            except urllib2.HTTPError:
                return False
        
        tree = ElementTree.parse(fh)
        runs = tree.findall('run/runnumber')
        run_xmls = tree.findall('run/runindex')
        
        for i, run in enumerate(runs):
            self.run_index[run.text] = run_xmls[i].text
            self.run_list[run.text] = '1'
        
        return True
    
    def _load_info(self):
        '''load single run diagnostics info'''
        if not self.run_list.get(self.runno, '') :
            return False
        self.info['base_url'] = self.base_url
        self.info['xml_base_url'] = self.xml_base_url
        self.info['run_xml'] = self.run_index[self.runno]
        self.info['rootfile_dir'] = os.path.dirname(self.info['run_xml']) + '/root'
        self.info['detectors'] = {}
        self.info['channels'] = {}
        
        try:
            fh = open(os.path.join(self.local_base_dir, self.info['run_xml']))
            self.info['load_from'] = 'local'
        except IOError:
            try:
                fh = urllib2.urlopen(self.xml_base_url + self.info['run_xml'])
                self.info['load_from'] = 'remote'
            except urllib2.HTTPError:
                return False
                
        tree = ElementTree.parse(fh)
        for detectorNode in tree.findall('run/detector'):
            detname = detectorNode.find('detname').text
            self.info['detectors'][detname] = []
            self.info['channels'][detname] = {}
            for figureNode in detectorNode.findall('figure'):
                figure_info = {}
                figure_info['figname'] = figureNode.find('figname').text
                figure_info['figpath'] = figureNode.find('path').text
                self.info['detectors'][detname].append(figure_info)
            for channelNode in detectorNode.findall('channel'):
                channelname = channelNode.find('channelname').text
                channelname = channelname.replace('board', '')
                channelname = channelname.replace('connector', '')
                self.info['channels'][detname][channelname] = '1'


    def figure_choices(self):
        '''return a Field.Choices of available figures'''
        import os
        dirname = os.path.realpath(os.path.dirname(__file__))
        filename = os.path.join(dirname, 'ref', 'diagnostics_figs.ref')
        try:
            fh = open(filename)
        except IOError:
            return None
        figtypes = {
            'Basic' : 0,
            'AD' : 1,
            'Muon' : 2,
        }
        choices = ( 
            ('Basic', []), 
            ('AD', []), 
            ('Muon', []), 
        )
        for line in fh:
            figtype, figname = line.strip().split()
            choices[figtypes[figtype]][1].append((figname, figname))
                
        return choices
                   