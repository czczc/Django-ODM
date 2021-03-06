# Managing PQM info
import urllib2, rfc822, os.path
from django.conf import settings

class Pqm(object):
    '''class to manage PQM info '''
    
    base_url = 'http://web.dyb.ihep.ac.cn/dqm/'
    runlist_file = 'HistLog/available_run_number'
    runlist_local = settings.PROJECT_PATH+'/../tmp/pqmlist.txt'
    RPC_ordered_figs = [
            'SysTrigRate',     'Rate4Fold', 'DeltaTrigTime', 
                 'ErrFec',     'LayerMult', 'Delta4FoldTime', 
                 'ErrRtm',    'ModuleMult', 'Delta4FoldLogTime', 
           '4FoldMapRate', '4FoldMapPatch', '4FoldMultMap', 
        'EfficiencyStats',           'Hit', 'NoiseRateStats',
        'EfficiencyMapL1',      'HitMapL1', 'NoiseRateMapL1', 
        'EfficiencyMapL2',      'HitMapL2', 'NoiseRateMapL2', 
        'EfficiencyMapL3',      'HitMapL3', 'NoiseRateMapL3',
        'EfficiencyMapL4',      'HitMapL4', 'NoiseRateMapL4'
    ]
    
    def __init__(self, runno=''):
        self.runno = runno
        self.run_index = {}    # {runno: sum_file}
        self.run_list  = {}    # {runno: 1}
        self._load_index()
        
        # info dictionary intended for json serializer
        self.info = {
            'base_url' : '',
            'figure_summary' : '',
            'site' : '',
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
    
    def _load_from_file(self, fh):
        for line in fh:
            runno = line.strip().split()[0]
            self.run_list[runno] = '1'
            self.run_index[runno] = 'HistLog/run' + runno + '/available_plots.txt'
                     
    def _load_index(self):
        '''load pqm run list'''
        try:
            fh = urllib2.urlopen(self.base_url + self.runlist_file)
        except (urllib2.HTTPError, urllib2.URLError):
            return False
        
        # from pprint import pprint
        # pprint(fh.info().__dict__)
        # remote_filetime = rfc822.mktime_tz(rfc822.parsedate_tz(fh.info()['Last-Modified']))
        # local_filetime  = os.path.getmtime(self.runlist_local)
        # print remote_filetime
        # # print fh.info()['Last-Modified']
        # print local_filetime
        
        remote_filesize = int(fh.info()['content-length'])
        local_filesize  = int(os.path.getsize(self.runlist_local))
        # print remote_filesize
        # print local_filesize
       
        if (local_filesize == remote_filesize):
            f = open(self.runlist_local)
            self._load_from_file(f)
        else:            
            # print 'reload'
            f = open(self.runlist_local, 'w')
            f.write(fh.read())
            f.close()
            f = open(self.runlist_local)
            self._load_from_file(f)
            
        # 
        # lines = fh.readlines()
        # for line in lines:
        #     runno = line.strip().split()[0]
        #     self.run_list[runno] = '1'
        #     self.run_index[runno] = 'HistLog/run' + runno + '/available_plots.txt'
        
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
            self.info['site'] = site
            detname = site + detector
            figure_info = {}
            figure_info['figname'] = figname
            figure_info['figpath'] = figpath
            self.info['detectors'].setdefault(detname, []).append(figure_info)
        
        self._sort_RPC()
    
    def _sort_RPC(self):
        figname_list = []
        figpath_list = []
        detname = self.info['site'] + 'RPC'
        try:
            for item in self.info['detectors'][detname]:
                figname_list.append(item['figname'])
                figpath_list.append(item['figpath'])
        except KeyError:
            return
                    
        ordered_figure_info = []
        # append figs acoording to predefined order
        for figname in self.RPC_ordered_figs:
            try:
                index = figname_list.index(figname)
                ordered_figure_info.append({
                    'figname' : figname_list[index],
                    'figpath' : figpath_list[index],
                })
                figname_list.pop(index)
                figpath_list.pop(index)
            except ValueError:
                pass
        # append rest of figs
        for index, figname in enumerate(figname_list):
            ordered_figure_info.append({
                'figname' : figname_list[index],
                'figpath' : figpath_list[index],
            })
        self.info['detectors'][detname] = ordered_figure_info
        
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
