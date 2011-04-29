from django.db import models
from django.conf import settings

#=====================================
class Run(models.Model):
    runno = models.IntegerField(unique=True)
    runtype = models.CharField(max_length=96)
    timestart = models.DateTimeField()
    timeend = models.DateTimeField()
    
    class Meta:
        ordering = ['-runno']
        
    def __unicode__(self):
        return u'run %d' % (self.runno, )
    
    def get_absolute_url(self):
        return "%s/local/run/%i/" % (settings.SITE_ROOT, self.runno)
