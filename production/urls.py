from django.conf.urls.defaults import *

urlpatterns = patterns('odm.production.views',

    # normal urls
    (r'^(\w+)/view/$', 'view'),
    (r'^diagnostics/run/(?P<runno>\d+)/(?P<site>\w+)/(?P<detector>\w+)/board/(?P<board>\d+)/connector/(?P<connector>\d+)', 'diagnostics_channel'),
    (r'^diagnostics/clean/tmp/$', 'diagnostics_cleantmp'),
    
    # ajax only urls
    (r'^diagnostics/run/list/', 'diagnostics_runlist'),
    (r'^diagnostics/run/(\d+)/', 'diagnostics_run'),
    
    
    (r'^pqm/run/list/', 'pqm_runlist'),
    (r'^pqm/run/(\d+)/', 'pqm_run'),
    
    (r'^simulation/run/(\d+)/', 'simulation_run'),
    
    (r'^(\w+)/search/run/(\d+)/', 'search'),
    
)