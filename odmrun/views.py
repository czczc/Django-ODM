from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
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
def notes(request, year=None, month=None, page=1, records=40):
    '''notes monthly archived view'''
    from django.contrib.comments.models import Comment
    from django.views.generic.date_based import archive_index, archive_month
    
    month_list = Comment.objects.dates('submit_date', 'month')[::-1]
    
    if (not year) or (not month):
        comment_list = Comment.objects.all().order_by('-submit_date')[:40]
        description = 'latest'
        base_url = settings.SITE_ROOT + '/run/notest/latest'
    
    else:
        comment_list = Comment.objects.all(
            ).filter(submit_date__year=int(year), submit_date__month=int(month)
            ).order_by('-submit_date')
        description = ''
        base_url = settings.SITE_ROOT + '/run/notes/' + year + '/' + month
        
    return object_list(request, 
        template_name = 'local/run/archived_notes.html',
        queryset = comment_list, 
        template_object_name = 'comment',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'description' : description,
            'month_list' : month_list,
            'count'        : comment_list.count(),  # total count, not per page
            'base_url'     : base_url,
        })
            
