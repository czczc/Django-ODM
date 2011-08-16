from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.core.paginator import Paginator
from django.conf import settings

from odm.runinfo.models import Daqruninfo, Daqcalibruninfo, Daqruninfovld
from odm.fileinfo.models import Daqrawdatafileinfo
from odm.odmrun.models import Run
from odm.runinfo.forms import SearchRunListForm, SearchCalibRunListForm

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
        elif search_term.startswith('monitor'):
            postfix = '/monitor/'
            search_term = search_term.replace('monitor', '', 1)
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
    '''single run detailed view'''
        
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
    
    calibrun_list = None
    if (run.runtype == 'ADCalib'):
        calibrun_list = Daqcalibruninfo.objects.filter(runno=runno)
        for calibrun in calibrun_list:
            calibrun.humanize()
        # try:
        #     calibrun = Daqcalibruninfo.objects.filter(runno=runno)[0]
        #     calibrun.humanize()
        # except:
        #     calibrun = None
    
    odmrun = None
    try:
        odmrun = Run.objects.get(runno=runno)
    except:
        odmrun = None

    return direct_to_template(request,
        template = 'run/detail.html', 
        extra_context = { 
            'run' : run,
            'num_files' : num_files, 
            'calibrun_list' : calibrun_list,
            'odmrun' : odmrun,
            'next' : run.get_absolute_url(),
        })


@login_required
def runlist(request, page=1, records=500):
    '''query run list from request.GET'''
    
    run_list = Daqruninfo.objects.select_related().all()
    
    if request.GET:
        description = 'Search'
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
        description = 'All'
        form = SearchRunListForm() # unbound form
    
   
    return object_list(request, 
        template_name = 'run/list.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'form'         : form,
            'description'  : description,
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
def calibration(request, sourcetype, page=1, records=100):
    '''query by calibration source type'''
    run_list = Daqcalibruninfo.objects.list_sourcetype(sourcetype)
    description = {
        'Ge68' : '<sup>68</sup>Ge',
        'AmC_Co60' : '<sup>241</sup>Am<sup>13</sup>C + <sup>60</sup>Co',
        'MO_LED' : 'MO LED',
        'ACU_LED' : 'ACU LED',
        'Double_Pulse' : 'Double Pulse',
    } 
    
    if request.GET:
        form = SearchCalibRunListForm(request.GET) # bound form
        if form.is_valid():
            
            if form.cleaned_data['site'] != 'All' and form.cleaned_data['detector'] != 'All':
                detector =  form.cleaned_data['site'] + '-' + form.cleaned_data['detector']
                from odm.conventions.conf import Site
                detectorid = Site.daq_id.get(detector, 0)
                run_list = run_list.filter(detectorid=detectorid)
                
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
        form = SearchCalibRunListForm() # unbound form
        
        
    return object_list(request, 
        template_name = 'run/calibration/list.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'form'         : form,
            'sourcetype'   : sourcetype,
            'description'  : description.get(sourcetype, 'Unknown'),
            'count'        : run_list.count(),  # total count, not per page
            'base_url'     : settings.SITE_ROOT + '/run/calibration/' + sourcetype,
            'query_string' : '?' + request.META.get('QUERY_STRING', '')
        })


@login_required
def calibrun(request, runno, adno=1):
    '''details of calibration raw parameters'''
    from django.utils.datastructures import SortedDict
    info = {}
    try:
        run = Daqcalibruninfo.objects.get(runno=runno, adno=adno)
    except:
        return HttpResponse(json.dumps(info))
    
    info = SortedDict((x.name, x.value_to_string(run)) for x in run._meta.fields)
    if request.is_ajax():
        return HttpResponse(json.dumps(info))
    else:
        return HttpResponse('<pre>'+ json.dumps(info, indent=4) + '</pre>')

    
@login_required
def archive(request, year=None, month=None, page=1, records=500):
    '''monthly archived view'''
    
    month_list = Daqruninfovld.objects.dates('timestart', 'month')[::-1]
    
    if (not year) or (not month):
        run_list = Daqruninfo.objects.select_related().all()[:100]
        description = 'Latest'
        base_url = settings.SITE_ROOT + '/run/archives/latest'
    
    else:
        run_list = Daqruninfo.objects.select_related().all(
            ).filter(vld__timestart__year=int(year), vld__timestart__month=int(month)
            )
        description = ''
        base_url = settings.SITE_ROOT + '/run/archive/' + year + '/' + month
        
    return object_list(request, 
        template_name = 'run/archive.html',
        queryset = run_list, 
        template_object_name = 'run',
        paginate_by = int(records),
        page = int(page),
        extra_context = {
            'description' : description,
            'month_list' : month_list,
            'count'        : run_list.count(),  # total count, not per page
            'base_url'     : base_url,
        })

@login_required
def stats(request, mode='runcount'):
    '''graphical stats'''          
    if not request.is_ajax():
        # return HttpResponse('<pre>'+ json.dumps(integrated_info, indent=4) + '</pre>')
        return direct_to_template(request, 
            template = 'run/stats.html',
            extra_context = {
            })
    
    # ajax response
    raw_info = {
        # year-month : nRuns,
    }
    info = {
        'xformat' : 'year-month',
        'xpoints' : [],
        'ypoints' : [],
        'title'   : '',
        'ytitle'  : '',
        'legend'  : '',
    }
    if mode == 'runcount':
        run_list = Daqruninfo.objects.select_related()
        for run in run_list:
            date = run.vld.timestart
            key = "%04d-%02d" % (date.year, date.month)
            raw_info.setdefault(key, 0)
            raw_info[key] = raw_info[key] + 1
        info['title'] = 'Integrated Number of Runs'
        info['ytitle'] = 'Runs'
        info['legend'] = 'All Runs'
    elif mode == 'daqtime':
        from datetime import timedelta
        run_list = Daqruninfo.objects.select_related().exclude(partitionname='part_eh1-rpc')
        for run in run_list:
            date = run.vld.timestart
            key = "%04d-%02d" % (date.year, date.month)
            raw_info.setdefault(key, timedelta())
            raw_info[key] = raw_info[key] + run.vld.runlength()
        info['title'] = 'Integrated DAQ Time'
        info['ytitle'] = 'Days'
        info['legend'] = 'All Runs'
    elif mode == 'partition':
        from django.db.models import Count
        value_list = Daqruninfo.objects.values('partitionname').annotate(count=Count('partitionname'))
        xpoints = []
        ypoints = []
        for value in value_list:
            xpoints.append(value['partitionname'][5:].upper())
            ypoints.append(value['count'])
        total = sum(ypoints)
        for i in range(len(ypoints)):
            ypoints[i] = float(ypoints[i]) * 100 / total
            if ypoints[i] > 0.5:
                info['xpoints'].append(xpoints[i])
                info['ypoints'].append(float('%.1f' % (ypoints[i], )))
        info['title'] = 'DAQ Partition Shares'
        info['ytitle'] = ''
        info['legend'] = 'DAQ Partition Shares'
        info['xformat'] = 'category'
        return HttpResponse(json.dumps(info))
    elif mode == 'runtype':
        from django.db.models import Count
        value_list = Daqruninfo.objects.values('runtype').annotate(count=Count('runtype'))
        xpoints = []
        ypoints = []
        for value in value_list:
            xpoints.append(value['runtype'])
            ypoints.append(value['count'])
        total = sum(ypoints)
        for i in range(len(ypoints)):
            ypoints[i] = float(ypoints[i]) * 100 / total
            if ypoints[i] > 0.5:
                info['xpoints'].append(xpoints[i])
                info['ypoints'].append(float('%.1f' % (ypoints[i], )))
        info['title'] = 'Run Type Shares'
        info['ytitle'] = ''
        info['legend'] = 'Run Type Shares'
        info['xformat'] = 'category'
        return HttpResponse(json.dumps(info))
    else:
        return HttpResponse(json.dumps(raw_info)) # empty
            
    for key in sorted(raw_info):
        info['xpoints'].append(key)
        info['ypoints'].append(raw_info[key])
    
    for i in range(len(info['xpoints'])):
        if i > 0:
            info['ypoints'][i] += info['ypoints'][i-1]
    
    if mode == 'daqtime':
        for i in range(len(info['xpoints'])):
            info['ypoints'][i] = info['ypoints'][i].days
            
    return HttpResponse(json.dumps(info))


@login_required
def daqinfo(request, runno):
    '''json daqinfo info'''
    
    from odm.daqinfo.models import Daqrunconfig
    
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
            
    if request.is_ajax():
        return HttpResponse(json.dumps( Daqruninfo.objects.json_listall() ))
    else:
        return HttpResponse('<pre>'+ json.dumps(Daqruninfo.objects.json_listall(), indent=4) + '</pre>')

        
@login_required
def monitor(request, runno):
    '''single run monitor'''
            
    return direct_to_template(request,
        template = 'run/monitor.html', 
        extra_context = { 
            'runno' : runno,
        })

@login_required
def site_monitor(request, site):
    '''single run monitor'''
    x = Daqrawdatafileinfo.objects.filter(filename__icontains=site+'-Merged'
        ).exclude(filename__icontains='test')[:1]
    if x:
        return direct_to_template(request,
            template = 'run/monitor.html', 
            extra_context = { 
                'runno' : x[0].runno,
                'filename' : x[0].filename,
                'timeend_beijing' : x[0].vld.timeend_beijing(),
            })
    else:
        return HttpResponse('no file found for ' + site + '-Merged')
        