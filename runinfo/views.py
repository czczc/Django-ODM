from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from django.core.paginator import Paginator

from odm.runinfo.models import Daqruninfo

def run(request, run):
    # mylist = Daqruninfo.objects.get(runno=run)
    runinfo = Daqruninfo.objects.get(runno=run)
    return HttpResponse(u'%s' % (runinfo.seqno.timestart,))

# @login_required
# def runtype(request, runtype='All', page=1, records=500):        
#     return object_list(request, 
#         template_name = 'runinfo/runlist.html',
#         queryset = Daqruninfo.objects.list_runtype(runtype), 
#         template_object_name = 'run',
#         paginate_by = int(records),
#         page = int(page),
#         extra_context = {
#             'runtype' : runtype,
#             'base_url' : '/runtype/' + runtype,
#         })

    