from django.conf.urls.defaults import *

urlpatterns = patterns('odm.odmrun.views',
    # single run
    (r'^run/(\d+)/$', 'run'),
    
    # list
    (r'^run/notes/(?P<records>\d+)/', 'notes'),    
    (r'^run/notes/$', 'notes'),    
)