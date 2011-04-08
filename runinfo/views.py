from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.core.paginator import Paginator
from django.conf import settings

from odm.runinfo.models import Daqruninfo, Daqcalibruninfo
from odm.daqinfo.models import Daqrunconfig

import json, re

@login_required
def quick_search(request):
    '''quick search box'''
    
    runno = ''
    postfix = ''
    
    if request.method == 'POST':
        search_term = request.POST.get('search_term', '').lower()
        if search_term.startswith('sim'): 
            postfix = '/sim/'
            search_term = search_term.replace('sim', '', 1)
        try:
            runno = re.search(r'(\d+)', search_term).group(1)            
        except:
            return HttpResponse('sorry, invalid search')
            
        if postfix:
            return HttpResponseRedirect(settings.SITE_ROOT + '/run/' + runno + postfix)            
        else:
            return HttpResponseRedirect(settings.SITE_ROOT + '/run/' + runno)
    
    else:
        return HttpResponseRedirect(settings.SITE_ROOT + '/run/')


@login_required
def simrun(request, runno):
    '''query a simulation run'''
    return render_to_response('run/simulation.html', { 
        'runno' : runno, },
        context_instance=RequestContext(request))
        
            
@login_required
def run(request, runno, is_sim=''):
    '''query a single run'''
        
    run = get_object_or_404(Daqruninfo, runno=runno)
    calibrun = None
    if (run.runtype == 'ADCalib'):
        try:
            calibrun = Daqcalibruninfo.objects.get(runno=runno)
            calibrun.humanize()
        except:
            calibrun = None
    return render_to_response('run/detail.html', { 
        'run' : run, 
        'calibrun' : calibrun },
        context_instance=RequestContext(request))


@login_required
def latest(request, days='7', page=1, records=500):
    '''query by latest days'''
    
    run_list = Daqruninfo.objects.list_latest(days)
    return object_list(request, 
        template_name = 'run/list.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'description'  : 'Latest-' + days + '-day',
            'count'        : run_list.count(),  # total count, not per page
            'base_url'     : settings.SITE_ROOT + '/run/latest/days/' + days,
        })


@login_required
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


@login_required
def daqinfo(request, runno):
    '''json daqinfo info'''
    
    Daqrunconfig.objects.runno = runno
    Daqrunconfig.objects.fetch_all()
    
    # for debug
    # return HttpResponse('<pre>'+ json.dumps(Daqrunconfig.objects.info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(Daqrunconfig.objects.info))
    else:
        raise Http404
        
@login_required
def jsonlist(request):
    '''json list run info'''
        
    # for debug
    # return HttpResponse('<pre>'+ json.dumps(Daqruninfo.objects.json_listall(), indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps( Daqruninfo.objects.json_listall() ))
    else:
        raise Http404
        