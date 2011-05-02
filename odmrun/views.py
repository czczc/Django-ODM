from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.conf import settings

from odm.odmrun.models import Run

@login_required
def run(request, runno):
    '''detailed view of Run object'''
        
    try:
        run = Run.objects.get(runno=runno)
    except:
        return direct_to_template(request, 
            template = 'local/run/detail.html',
            extra_context = {
                'not_in_local_db' : True,
                'run' : {'runno' : runno},
            })

    return direct_to_template(request, 
        template = 'local/run/detail.html',
        extra_context = {
            'run' : run,
        })

@login_required
def notes(request, records=10):
    '''list view pagenated notes'''
    from django.contrib.comments.models import Comment
    from django.views.generic.list_detail import object_list
    from django.db.models import Count
    
    comment_list = Comment.objects.order_by('-submit_date')[:records]

    return object_list(request, 
        template_name = 'local/run/notes.html',
        queryset = comment_list,
        template_object_name = 'comment',
        extra_context = {
        })