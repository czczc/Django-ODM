from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dbi.views',
    
    (r'^records/$', 'records'),
    
    (r'^trend/$', 'trend'),
    (r'^trend/(?P<model>\w+)/$', 'trend'),
)