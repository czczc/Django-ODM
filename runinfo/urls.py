from django.conf.urls.defaults import *

urlpatterns = patterns('odm.runinfo.views',
    (r'^type/(?P<runtype>\w+)/page/(?P<page>\d+)/records/(?P<records>\d+)', 'runtype'),
    (r'^type/(\w+)/', 'runtype'),
    (r'^$', 'runtype'),
    
    (r'^test/(\d+)/$', 'test'),
)