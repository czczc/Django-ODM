from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
import os

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    (r'^test/$', direct_to_template, { 'template': 'test.html' }),
)

# media files
if settings.SITE_LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', 
            {'document_root': os.path.join(settings.PROJECT_PATH, 'media')}),
    )

# raise ValueError
