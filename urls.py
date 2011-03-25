from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import os

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, { 'template': 'index.html', }),
    (r'^test/$', direct_to_template, { 'template': 'test.html' }),
)

from odm import settings
# media files
if settings.SITE_LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', 
            {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
    )

# raise ValueError
