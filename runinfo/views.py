from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from django.core.paginator import Paginator

from odm.runinfo.models import Daqruninfo

def test(request, runno):
    # mylist = Daqruninfo.objects.get(runno=run)
    runinfo = Daqruninfo.objects.get(runno=runno)
    return HttpResponse(u'%s' % (runinfo.vld.timestart,))

# @login_required
def runtype(request, runtype='All', page=1, records=500):
           
    return object_list(request, 
        template_name = 'run/list.html',
        queryset = Daqruninfo.objects.list_runtype(runtype), 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'runtype' : runtype,
        })
