from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.comments.models import Comment

from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

# =====================================
class TaggedRun(TaggedItemBase):
    content_object = models.ForeignKey('Run')


class Run(models.Model):
    runno = models.IntegerField(unique=True)
    runtype = models.CharField(max_length=96)
    timestart = models.DateTimeField()
    timeend = models.DateTimeField()
    
    comments = generic.GenericRelation(Comment, object_id_field='object_pk')
    tags = TaggableManager(through=TaggedRun)
    
    class Meta:
        ordering = ['-runno']
        
    def __unicode__(self):
        return u'run %d' % (self.runno, )
    
    def get_absolute_url(self):
        return "%s/run/%i/" % (settings.SITE_ROOT, self.runno)

