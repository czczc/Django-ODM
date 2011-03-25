from django.conf.urls.defaults import *

urlpatterns = patterns('odm.runinfo.views',
    (r'^type/(\w+)/', 'runtype'),
    (r'^$', 'runtype'),
    
    (r'^test/(\d+)/$', 'test'),
)