from django.conf.urls.defaults import *

urlpatterns = patterns('odm.odmrun.views',
    # single run
    (r'^run/(\d+)/$', 'run'),  
)