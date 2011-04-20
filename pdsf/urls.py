from django.conf.urls.defaults import *

urlpatterns = patterns('odm.pdsf.views',

    (r'users/$', 'users'),
    (r'user/(\w+)/$', 'user'),
    
)
