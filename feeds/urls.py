from django.conf.urls.defaults import *

from odm.runinfo.feeds import LatestRunFeed
from odm.odmrun.feeds import LatestCommentFeed

urlpatterns = patterns('',
    (r'^run/latest/$', LatestRunFeed()),
    (r'^run/notes/latest/$', LatestCommentFeed()),
)