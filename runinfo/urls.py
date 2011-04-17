from django.conf.urls.defaults import *

urlpatterns = patterns('odm.runinfo.views',
    # single run
    (r'^(\d+)/$', 'run'),
    (r'^(\d+)/sim/$', 'simrun'),
    
    # query run list
    (r'^list/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'runlist'),
    (r'^list/', 'runlist'),
    
    # list by run type
    (r'^type/(?P<runtype>\w+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'runtype'),
    (r'^type/(\w+)/', 'runtype'),
    (r'^$', 'runtype'),
    
    (r'^latest/days/(?P<days>\d+)/page/(?P<page>\d+)/records/(?P<records>\d+)/', 'latest'),
    (r'^latest/days/(?P<days>\d+)', 'latest'),
    (r'^latest/days/', 'latest'),
    
    # ajax urls
    (r'^daq/(\d+)/', 'daqinfo'),
    (r'^json/list/$', 'jsonlist'),
    
)

urlpatterns += patterns('odm.fileinfo.views',
    (r'^(\d+)/files/$', 'fileinfo'),

    # ajax urls
    (r'^file/list/$', 'rawfilelist'),
    (r'^(\d+)/files/catalog/$', 'catalog'),
    (r'^(\d+)/files/diagnostics/$', 'diagnostics'),
   
)