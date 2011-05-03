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
def notes_archive(request, year=None, month=None):
    '''notes monthly archived view'''
    from django.contrib.comments.models import Comment
    from django.views.generic.date_based import archive_index, archive_month
    
    month_list = Comment.objects.dates('submit_date', 'month')[::-1]
    
    if (not year) or (not month):
        return direct_to_template(request, 
            template = 'local/run/archived_notes.html',
            queryset = Comment.objects.all(),
            extra_context = {
                'comment_list' : Comment.objects.all().order_by('-submit_date')[:20],
                'description' : 'Latest',
                'month_list' : month_list,
            })
    
    else:
        return archive_month(request, 
            template_name = 'local/run/archived_notes.html',
            template_object_name = 'comment',
            queryset = Comment.objects.select_related().order_by('-submit_date'),
            date_field = 'submit_date',
            year = year,
            month = month,
            extra_context = {
                'description' : month + ' ' + year,
                'month_list' : month_list,
            })

    
       
        