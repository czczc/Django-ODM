from odm.runinfo.models import Daqruninfo
from odm.odmrun.models import Run
from django.contrib.comments.models import Comment
from datetime import datetime, timedelta

# ====================================================
class RunScraper(object):
    
    def __init__(self, runmin=0, runmax=100000):
        self.runmin = runmin
        self.runmax = runmax
        
    def scrape_basic(self, dryrun=False):
        '''scrape basic run info from offline_db'''
        
        daqrunlist = Daqruninfo.objects.select_related().filter(
            runno__gte=self.runmin, runno__lte=self.runmax).order_by('runno')
        runno_list = set(run.runno for run in Run.objects.filter(
            runno__gte=self.runmin, runno__lte=self.runmax))
        
        run_count = 0;
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
                run_count += 1
                if dryrun:
                    import pprint
                    pprint.pprint(run.__dict__) 
                else:
                    run.save()
                    print 'run %d scraped' % runno
        
        print "\n=========\n", run_count, 'runs scraped'


# ====================================================
class CommentScraper(object):
    
    def __init__(self, runmin=0, runmax=100000):
        self.runmin = runmin
        self.runmax = runmax
        
    def scrape_daq_csv(self, dryrun=False):
        '''scrape comments from daq run list excel files'''
        from django.conf import settings
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth.models import User
        from django.contrib.sites.models import Site
        import os, glob, csv
        
        csv_list = glob.glob(settings.PROJECT_PATH + '/data/runlist/*.csv')
        runno_list = set(run.runno for run in Run.objects.filter(
            runno__gte=self.runmin, runno__lte=self.runmax))
        content_type = ContentType.objects.get(name='run')
        user = User.objects.get(username='daq')
        site = Site.objects.all()[0]
        
        run_count = 0;
        for csv_file in csv_list:
            reader = csv.DictReader(open(csv_file, "rU"))
            primary_fields = ['RunNumber', 'RunType', 'TriggerType', 'DataCategory', 'Description', 'Comments']
            exclude_fields = []
            exclude_values = ['NULL', '0', '~', '', '?', 'None']
            remaining_fields = sorted(set(reader.fieldnames) - set(primary_fields) - set(exclude_fields))
            for row in reader:
                try:
                    runno = int(row.get('RunNumber', 0))
                except ValueError:
                    continue # not a number
                
                if not (runno in runno_list): continue
                run = Run.objects.select_related().get(runno=runno)
                try:
                    comment = run.comments.order_by('submit_date')[0]
                    if comment.user.username == 'daq':
                        print 'run ', run.runno, ' skipped'
                        continue # already posted
                except IndexError:
                    # no comments yet, continue to post
                    pass
                run_count += 1
                
                notes = ''
                notes += self._format_table_head(div_class='grid_12', header='Notes')
                for field in primary_fields:
                    value = row.get(field, '')
                    if value in exclude_values: continue
                    notes += self._format_table_row(field, value)
                notes += self._format_table_foot()
                
                notes += self._format_table_head(div_class='grid_9', header='Extra Notes')
                for field in remaining_fields:
                    value = row.get(field, '')
                    if value in exclude_values: continue
                    if not field: field = 'P.S.'
                    notes += self._format_table_row(field, value)    
                notes += self._format_table_foot()
                
                # clear div
                notes += "<div class='clear'></div>\n"
                self.save_run_comment(
                    content=notes, 
                    content_type=content_type, 
                    run=run, 
                    user=user, 
                    site=site,
                    dryrun=dryrun)
                
        print "\n=========\n", run_count, 'runs updated'

    def save_run_comment(self, content, content_type, run, user, site, dryrun):
        '''add/update comment'''
        comment = Comment(
            comment=content,
            content_type=content_type,
            object_pk = run.pk,
            site = site,
            user = user,
            user_name = user.username,
            user_email = user.email,
            user_url = '',
            submit_date = run.timeend, # UTC
        )
        if dryrun:
            import pprint
            pprint.pprint(comment.__dict__)
        else:
            comment.save()
            print 'run ', run.runno, ' updated'
        
        
    def _format_table_head(self, div_class, header):
        html = "<div class='" + div_class + "'><table>\n"
        html += "<thead><tr><th colspan='2' style='text-align: center;'>" + header + "</th></tr></thead>\n"
        html += "<tbody>"
        return html
        
    def _format_table_row(self, field, value):
        html = "<tr><td class='descr'>%s</td><td class='value'>%s</td></tr>\n" % (field, value)
        return html
        
    def _format_table_foot(self):
        html = "</tbody></table></div>\n"
        return html
        