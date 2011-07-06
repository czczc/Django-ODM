from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dcs.views',
    (r'^monitor/(?P<site>\w+)/$', 'monitor'),
    
    # ajax data
    (r'^data/(?P<model>\w+)/latest/days/(?P<latest_days>\d+)/$', 'data'),
    (r'^data/(?P<model>\w+)/$', 'data'),
    
    (r'^record/(?P<model>\w+)/last/$', 'fetchone'),
)
