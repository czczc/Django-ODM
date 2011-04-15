from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.core.paginator import Paginator
from django.conf import settings

from odm.runinfo.models import Daqruninfo, Daqcalibruninfo
from odm.daqinfo.models import Daqrunconfig
from odm.fileinfo.models import Daqrawdatafileinfo
from odm.runinfo.forms import SearchRunListForm

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
        elif search_term.startswith('files'):
            postfix = '/files/'
            search_term = search_term.replace('files', '', 1)
        
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
def run(request, runno):
    '''query a single run'''
        
    # run = get_object_or_404(Daqruninfo, runno=runno)
    try:
        run = Daqruninfo.objects.get(runno=runno)
    except:
        return direct_to_template(request, 
            template = 'run/detail.html',
            extra_context = {
                'not_in_offline_db' : True,
                'run' : {'runno' : runno},
            })
    num_files = Daqrawdatafileinfo.objects.filter(runno=runno).count()
    calibrun = None
    if (run.runtype == 'ADCalib'):
        try:
            calibrun = Daqcalibruninfo.objects.get(runno=runno)
            calibrun.humanize()
        except:
            calibrun = None
    return render_to_response('run/detail.html', { 
        'run' : run,
        'calibrun' : calibrun,
        'num_files' : num_files, 
        },
        context_instance=RequestContext(request))


@login_required
def runlist(request, page=1, records=500):
    '''query run list from request.GET'''
    
    run_list = Daqruninfo.objects.select_related().all()
    
    if request.GET:
        form = SearchRunListForm(request.GET) # bound form
        if form.is_valid():
            # partition
            if form.cleaned_data['site'] == 'All':              
                if not form.cleaned_data['detector'] == 'All':
                    detector = form.cleaned_data['detector']
                    partitionlist = []
                    for site in ['EH1', 'EH2', 'EH3', 'SAB']:
                        partitionlist.append('part_' + site + '-' + detector)
                    run_list = run_list.filter(partitionname__in=partitionlist)             
            else:
                partitionname = 'part_' + form.cleaned_data['site']
                if not form.cleaned_data['detector'] == 'All':
                    partitionname += '-' + form.cleaned_data['detector']
                run_list = run_list.filter(partitionname=partitionname)

            
            if not form.cleaned_data['runtype'] == 'All':
                run_list = run_list.filter(runtype=form.cleaned_data['runtype'])
            if form.cleaned_data['run_from']:
                run_list = run_list.filter(runno__gte=form.cleaned_data['run_from'])
            if form.cleaned_data['run_to']:
                run_list = run_list.filter(runno__lte=form.cleaned_data['run_to'])
            if form.cleaned_data['date_from']:
                run_list = run_list.filter(vld__timestart__gte=form.cleaned_data['date_from'])
            if form.cleaned_data['date_to']:
                run_list = run_list.filter(vld__timestart__lte=form.cleaned_data['date_to'])
            if form.cleaned_data['sort_run'] == 'ASC':
                run_list = run_list.order_by('runno')

        else:
            run_list = run_list.filter(runno=0) # hack, no match
    else:
        # return HttpResponse(json.dumps(request.GET, indent=4))
        form = SearchRunListForm() # unbound form
    
   
    return object_list(request, 
        template_name = 'run/list.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'form'         : form,
            'description'  : 'Search List',
            'count'        : run_list.count(),  # total count, not per page
            'base_url'     : settings.SITE_ROOT + '/run/list',
            'query_string' : '?' + request.META.get('QUERY_STRING', '')
        })


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
def fileinfo(request, runno):
    '''file info'''
        
    file_list = Daqrawdatafileinfo.objects.filter(runno=runno)
    return object_list(request, 
        template_name = 'run/file.html',
        queryset = file_list, 
        template_object_name = 'file',
        extra_context = {
            'runno'  : runno,
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

@login_required
def filelist(request):
    '''json list file info'''
    from django.db.models import Count
    file_list = Daqrawdatafileinfo.objects.values(
        'runno').annotate(num_files=Count('runno'))
    info = dict( (afile['runno'], afile['num_files']) for afile in file_list )
        
    # for debug
    # return HttpResponse('<pre>'+ json.dumps(info, indent=4) + '</pre>')

    if request.is_ajax():
        return HttpResponse(json.dumps(info))
    else:
        raise Http404
          