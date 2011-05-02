from django.contrib.syndication.views import Feed
from odm.runinfo.models import Daqruninfo

class LatestRunFeed(Feed):
    """Feed of latest daq runs"""
    
    title = 'ODM | DAQ Runs'
    link = 'https://portal-auth.nersc.gov/dayabay/odm/'
    description = 'Information on Latest DAQ Runs'

    def items(self):
        return Daqruninfo.objects.select_related()[:20]

    def item_pubdate(self, item):
        return item.vld.timeend

    def item_title(self, item):
        return '%s Run %d Finished' % (item.runtype, item.runno)

    def item_description(self, item):
        return item.summary()

    def item_link(self, item):
        return item.get_absolute_url()

