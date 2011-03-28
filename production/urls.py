from django.conf.urls.defaults import *

urlpatterns = patterns('odm.production.views',

    # ajax only urls
    (r'^diagnostics/run/list/', 'diagnostics_runlist'),
    (r'^diagnostics/run/(\d+)/', 'diagnostics_run'),
)