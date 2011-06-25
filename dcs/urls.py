from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dcs.views',
    (r'^(?P<site>\w+)/$', 'monitor'),
    
    # ajax data
    (r'^model/(?P<model>\w+)/$', 'data'),
)
