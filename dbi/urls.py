from django.conf.urls.defaults import *

urlpatterns = patterns('odm.dbi.views',
    
    (r'^records/$', 'records'),
        
    # (r'^calibpmtspec/(?P<site>\w+)/(?P<detector>\w+)/(?P<pmtid>\d+)/(?P<character>.)/$', 'dbi_calibpmtspec'),
    # (r'^calibpmtspec/(?P<site>\w+)/(?P<detector>\w+)/(?P<pmtid>\d+)/$', 'dbi_calibpmtspec'),
    # (r'^calibpmtspec/(?P<site>\w+)/(?P<detector>\w+)/(?P<character>.)/$', 'dbi_calibpmtspec'),
    # (r'^calibpmtspec/(?P<site>\w+)/(?P<detector>\w+)/$', 'dbi_calibpmtspec'),
    # 
    # (r'^cablemap/(?P<site>\w+)/(?P<detector>\w+)/(?P<sensorid>\d+)/(?P<character>.)/$', 'dbi_cablemap'),
    # (r'^cablemap/(?P<site>\w+)/(?P<detector>\w+)/(?P<sensorid>\d+)/$', 'dbi_cablemap'),
    # (r'^cablemap/(?P<site>\w+)/(?P<detector>\w+)/(?P<character>.)/$', 'dbi_cablemap'),
    # (r'^cablemap/(?P<site>\w+)/(?P<detector>\w+)/$', 'dbi_cablemap'),
)