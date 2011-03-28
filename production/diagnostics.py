# Managing diagnositcs info 
import urllib2
from xml.etree import ElementTree
import os
 
class Diagnostics(object):
    '''class to manage diagnositcs info '''
    
    xml_base_url = 'http://portal.nersc.gov/project/dayabay/dybprod/'
    runs_xml = 'http://portal.nersc.gov/project/dayabay/dybprod/runs.xml'
    
    def __init__(self, runno=''):
        self.runno = runno
        
        # base_url can be different from xml_base_url so that they can 
        # be served on diffrent servers
        if self.runno < '7000':
            self.base_url = 'http://blinkin.krl.caltech.edu/~chao/dybprod/'
        else:
            self.base_url = 'http://portal.nersc.gov/project/dayabay/dybprod/'
 	    
        self.run_index = {}    # {runno: xml}
        self.run_list  = {}    # {runno: 1} 
        self._load_index()
        
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
        }
        if (self.runno):
            self._load_info()
        
    def _load_index(self):
        '''load diagnostics run list'''
        try:
            fh = urllib2.urlopen(self.runs_xml)
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
        
        try:
            fh = urllib2.urlopen(self.xml_base_url + self.info['run_xml'])
        except urllib2.HTTPError:
            return False
        tree = ElementTree.parse(fh)
        for detectorNode in tree.findall('run/detector'):
            detname = detectorNode.find('detname').text
            self.info['detectors'][detname] = []
            for figureNode in detectorNode.findall('figure'):
                figure_info = {}
                figure_info['figname'] = figureNode.find('figname').text
                figure_info['figpath'] = figureNode.find('path').text
                self.info['detectors'][detname].append(figure_info)
         