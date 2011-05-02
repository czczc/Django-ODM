from django.conf.urls.defaults import *

from odm.odmrun.feeds import LatestCommentFeed

urlpatterns = patterns('',
    (r'^run/notes/latest/$', LatestCommentFeed(),)
)