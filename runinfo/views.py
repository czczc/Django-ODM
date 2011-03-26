from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.core.paginator import Paginator
from django.conf import settings

from odm.runinfo.models import Daqruninfo

def test(request, runno):
    runinfo = Daqruninfo.objects.get(runno=runno)
    return HttpResponse(u'%s' % (runinfo.vld.timestart,))


def run(request, runno):
    '''query a single run'''
    
    run = get_object_or_404(Daqruninfo, runno=runno)
    return render_to_response('run/detail.html',
        { 'run' : run, },
        context_instance=RequestContext(request))

# @login_required
def runtype(request, runtype='All', page=1, records=500):
    '''query by run type'''
    
    run_list = Daqruninfo.objects.list_runtype(runtype)
    return object_list(request, 
        template_name = 'run/list.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'description'  : runtype,
            'count'        : run_list.count(),  # total count, not per page
            'base_url'     : settings.SITE_ROOT + '/run/type/' + runtype,
        })
