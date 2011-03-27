# Managing diagnositcs info 
import urllib2
from xml.etree import ElementTree
 
class Diagnostics(object):
    '''class to manage diagnositcs info '''
    runs_xml = 'http://portal.nersc.gov/project/dayabay/dybprod/runs.xml'
    
    def __init__(self, runno):
        self.runno = runno
        self.run_index = {}    # {runno: xml}
        self.run_list  = {}    # {runno: 1} 
        
        self._make_index()
        
    def _make_index(self):
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