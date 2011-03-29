# Managing PQM info
import urllib2

class Pqm(object):
    '''class to manage PQM info '''
    
    base_url = 'http://web.dyb.ihep.ac.cn/dqm/'
    runlist_file = 'HistLog/available_run_number'
    
    def __init__(self, runno=''):
        self.runno = runno
        
        self.run_index = {}    # {runno: sum_file}
        self.run_list  = {}    # {runno: 1}
        self._load_index()
        
        
    def _load_index(self):
        '''load pqm run list'''
        try:
            fh = urllib2.urlopen(self.base_url + self.runlist_file)
        except urllib2.HTTPError:
            return False
        
        for line in fh:
            runno = line.strip()
            self.run_list[runno] = '1'
        
        return True