from django.conf import settings
from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.contrib import comments
from django.utils.translation import ugettext as _

class LatestCommentFeed(Feed):
    """Feed of latest comments on the current site."""
    
    title = 'ODM | DAQ Run Notes'
    link = 'https://portal-auth.nersc.gov/dayabay/odm/'
    description = 'Latest Description and Notes on DAQ Runs'

    def items(self):
        qs = comments.get_model().objects.filter(
            site__pk = settings.SITE_ID,
            is_public = True,
            is_removed = False,
        )
        if getattr(settings, 'COMMENTS_BANNED_USERS_GROUP', None):
            where = ['user_id NOT IN (SELECT user_id FROM auth_user_groups WHERE group_id = %s)']
            params = [settings.COMMENTS_BANNED_USERS_GROUP]
            qs = qs.extra(where=where, params=params)
        return qs.order_by('-submit_date')[:20]

    def item_pubdate(self, item):
        return item.submit_date

    def item_title(self, item):
        try:
            return '%s posted a note on Run %d' % (
                item.user.get_full_name(), item.content_object.runno)
        except:
            return '%s posted a note' % item.user.get_full_name()

    def item_description(self, item):
        return item.comment

    def item_link(self, item):
        return item.content_object.get_absolute_url() + '?c=' + str(item.id)

    def item_author_name(self, item):
        return item.user_name
                