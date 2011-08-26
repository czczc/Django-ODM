from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dcs.views',
    (r'^$', 'search'),

    (r'^monitor/(?P<site>\w+)/(?P<category>\w+)/$', 'monitor'),
    (r'^monitor/(?P<site>\w+)/$', 'monitor'),
    
    # ajax data
    (r'^data/(?P<model>\w+)/latest/days/(?P<latest_days>\d+)/$', 'data'),
    (r'^data/(?P<model>\w+)/$', 'data'),
    
    (r'^record/(?P<model>\w+)/last/$', 'fetchone'),
)
