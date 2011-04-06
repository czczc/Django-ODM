from django.conf.urls.defaults import *

urlpatterns = patterns('odm.production.views',

    # ajax only urls
    (r'^diagnostics/run/list/', 'diagnostics_runlist'),
    (r'^diagnostics/run/(\d+)/', 'diagnostics_run'),
    
    (r'^pqm/run/list/', 'pqm_runlist'),
    (r'^pqm/run/(\d+)/', 'pqm_run'),
    
    (r'^simulation/run/(\d+)/', 'simulation_run'),
    
    # normal urls
    (r'^(\w+)/view/$', 'view'),
)