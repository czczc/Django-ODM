from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

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

