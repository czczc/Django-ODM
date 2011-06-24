from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dcs.views',
    
    # ajax data
    (r'^(?P<model>\w+)/$', 'data'),
)
