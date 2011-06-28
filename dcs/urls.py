from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dcs.views',
    (r'^monitor/(?P<site>\w+)/$', 'monitor'),
    
    # ajax data
    (r'^data/(?P<model>\w+)/$', 'data'),
)
