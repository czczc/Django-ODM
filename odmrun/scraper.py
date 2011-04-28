from odm.runinfo.models import Daqruninfo
from odm.odmrun.models import Run

class RunScraper(object):
    
    def scrape_basic(self, min=0, max=100000):
        '''scrape basic run info from offline_db'''
        
        daqrunlist = Daqruninfo.objects.select_related().filter(
            runno__gte=min, runno__lte=max)
        runno_list = set(run.runno for run in Run.objects.filter(
            runno__gte=min, runno__lte=max))
        
        for daqrun in daqrunlist:
            runno = daqrun.runno
            if runno in runno_list: 
                continue
            else:
                run = Run(
                    runno = runno,
                    runtype = daqrun.runtype,
                    timestart = daqrun.vld.timestart,
                    timeend = daqrun.vld.timeend,
                )
                run.save()
                print 'run %d scraped' % runno
                