from django.conf.urls.defaults import *

urlpatterns = patterns('odm.pmtinfo.views',

    # ajax only urls
    (r'^(?P<site>\w+)/(?P<detector>\w+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', 
        'pmt'),

)