from django.conf.urls.defaults import *

urlpatterns = patterns('odm.pmtinfo.views',

    # ajax only urls
    # ajax only urls
    (r'^(?P<site>\w+)/(?P<detector>\w+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<rollback>\w+)/(?P<rollback_year>\d+)/(?P<rollback_month>\d+)/(?P<rollback_day>\d+)/', 
        'pmt'),
    (r'^(?P<site>\w+)/(?P<detector>\w+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', 
        'pmt'),

)