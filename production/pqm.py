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
        
        # info dictionary intended for json serializer
        self.info = {
            'base_url' : '',
            'figure_summary' : '',
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
        '''load pqm run list'''
        try:
            fh = urllib2.urlopen(self.base_url + self.runlist_file)
        except (urllib2.HTTPError, urllib2.URLError):
            return False
        
        for line in fh:
            runno = line.strip().split()[0]
            self.run_list[runno] = '1'
            self.run_index[runno] = 'HistLog/run' + runno + '/available_plots.txt'
        
        return True

    def _load_info(self):
        '''load single run PQM info'''
        if not self.run_list.get(self.runno, '') :
            return False
        self.info['base_url'] = self.base_url
        self.info['figure_summary'] = self.run_index.get(self.runno, 'not_exist')
        self.info['detectors'] = {}
        
        try:
            fh = urllib2.urlopen(self.base_url + self.info['figure_summary'])
        except (urllib2.HTTPError, urllib2.URLError):
            return False
                
        for line in fh:
            figname, figpath = line.split()
            site, detector = figpath.split('/')[2:4]
            detname = site + detector
            figure_info = {}
            figure_info['figname'] = figname
            figure_info['figpath'] = figpath
            self.info['detectors'].setdefault(detname, []).append(figure_info)


    def figure_choices(self):
        '''return a Field.Choices of available figures'''
        import os
        dirname = os.path.realpath(os.path.dirname(__file__))
        filename = os.path.join(dirname, 'ref', 'pqm_figs.ref')
        try:
            fh = open(filename)
        except IOError:
            return None
                    
        choices = ( ('Available Figures', []), )
        for line in fh:
            figname = line.strip()
            choices[0][1].append((figname, figname))
                
        return choices
