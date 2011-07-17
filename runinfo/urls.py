from django.conf.urls.defaults import *

urlpatterns = patterns('odm.runinfo.views',
    # single run
    (r'^(\d+)/$', 'run'),
    (r'^(\d+)/monitor/$', 'monitor'),
    (r'^(\d+)/sim/$', 'simrun'),
    
    # monitor
    (r'^monitor/(?P<site>\w+)/$', 'site_monitor'),
    
    # query run list
    (r'^list/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'runlist'),
    (r'^list/', 'runlist'),
    
    # list by run type
    (r'^type/(?P<runtype>\w+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'runtype'),
    (r'^type/(\w+)/', 'runtype'),
    (r'^$', 'runtype'),
    
    # calibration runs
    (r'^calibration/(\d+)/$', 'calibrun'),
    (r'^calibration/(?P<sourcetype>\w+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'calibration'),
    (r'^calibration/(\w+)/', 'calibration'),
    
    (r'^latest/days/(?P<days>\d+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'latest'),
    (r'^latest/days/(?P<days>\d+)/', 'latest'),
    (r'^latest/days/', 'latest'),

    # archives
    (r'^archive/(?P<year>\d+)/(?P<month>\d+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'archive'),
    (r'^archive/(?P<year>\d+)/(?P<month>\d+)/', 'archive'),
    (r'^archive/', 'archive'),
    
    # stats
    (r'^stats/(\w+)/', 'stats'),
    (r'^stats/', 'stats'),
    
    # ajax urls
    (r'^daq/(\d+)/', 'daqinfo'),
    (r'^json/list/$', 'jsonlist'),
    
)

urlpatterns += patterns('odm.fileinfo.views',
    (r'^(\d+)/files/$', 'fileinfo'),

    # ajax urls
    (r'^file/list/$', 'rawfilelist'),
    (r'^file/stats/(\w+)/$', 'stats'),
    (r'^(\d+)/files/catalog/$', 'catalog'),
    (r'^(\d+)/files/diagnostics/$', 'diagnostics'),
)

urlpatterns += patterns('odm.odmrun.views',
    (r'^notes/(?P<year>\d+)/(?P<month>\d+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'notes'),
    (r'^notes/(?P<year>\d+)/(?P<month>\d+)/', 'notes'),
    (r'^notes/latest/', 'notes'),
)

