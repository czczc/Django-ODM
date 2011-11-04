from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list
from django.conf import settings

from odm.fileinfo.models import Daqrawdatafileinfo

import json, os

@login_required
def fileinfo(request, runno):
    '''file info per run'''
        
    file_list = Daqrawdatafileinfo.objects.select_related().filter(runno=runno)
    return object_list(request, 
        template_name = 'run/file.html',
        queryset = file_list, 
        template_object_name = 'file',
        extra_context = {
            'runno'  : runno,
        })


@login_required
def catalog(request, runno):
    '''catalog file info per run'''
    if settings.SITE_IHEP:
        return HttpResponse(json.dumps({}))
        
    from DybPython import Catalog
    catalog_list = Catalog.runs[int(runno)]
    file_list = [ filename for filename in catalog_list ]
    info = {}
    if file_list:
        info['catalog_base_dir'] = os.path.dirname(file_list[0])
        info['files'] = dict( (os.path.basename(afile), 1) for afile in file_list )
    
    if request.is_ajax():
        return HttpResponse(json.dumps(info))
    else:
        return HttpResponse('<pre>'+ json.dumps(info, indent=4) + '</pre>')


@login_required
def diagnostics(request, runno):
    '''Diagnostics file info per run'''

    from odm.production.diagnostics import Diagnostics
    run = Diagnostics(runno)
    run.fetch_all()
    
    import glob, re
    info = {}
    rootfiel_dir = run.info.get('rootfile_dir', '')
    if rootfiel_dir:
        info['diagnostics_base_dir'] = os.path.join(run.local_base_dir, rootfiel_dir)
        info['files'] = {}
        file_list = glob.glob(info['diagnostics_base_dir'] + '/*.root')
        file_regex = re.compile(r'(.*)_run.*seq(\d+).root')
        for afile in file_list:
            filename = os.path.basename(afile)
            try:
                jobname, seq = file_regex.search(filename).group(1, 2)        
                info['files'].setdefault(seq, []).append(jobname)
            except:
                info['files'].setdefault('parsing_failed', []).append(filename)
    
    if request.is_ajax():
        return HttpResponse(json.dumps(info))
    else:
        return HttpResponse('<pre>'+ json.dumps(info, indent=4) + '</pre>')

        
@login_required
def rawfilelist(request):
    '''json raw file list (all runs)'''
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


@login_required
def stats(request, mode='volume', site='ALL'):
    '''graphical stats'''          
   
    # ajax response
    info = {
        'xpoints' : [],
        'ypoints' : [],
        'title'   : '',
        'ytitle'  : '',
        'legend'  : '',
    }
    
    xpoints = []
    ypoints = []
    from django.db.models import Sum
    if mode == 'volume':
        value_list = Daqrawdatafileinfo.objects.exclude(filename__contains='test'
            ).order_by('runno').values('runno'
            ).annotate(volume=Sum('filesize'))
        for value in value_list:
            xpoints.append(value['runno'])
            ypoints.append(value['volume']/1.1e12) # TB
        nRuns = len(xpoints)
        nPoints = 500
        step = int(nRuns/nPoints)+1            
        for i in range(nRuns):
            if i > 0:
                ypoints[i] += ypoints[i-1]
        info['xpoints'] = xpoints[::step]
        info['ypoints'] = ypoints[::step]
        for i in range(len(info['ypoints'])):
            info['ypoints'][i] = float('%.6f' % (info['ypoints'][i], ))            
        info['title'] = 'Integrated Data Volume'
        info['ytitle'] = 'Tera Bytes'
        info['legend'] = 'All Runs'
            
    elif mode == 'livetime':
        from django.utils.datastructures import SortedDict
        min_runno = 12400
        value_list = Daqrawdatafileinfo.objects.select_related(
            ).filter(filename__contains='Physics.'+site+'-Merged', runno__gte=min_runno
            ).order_by('runno'
            ).values('runno', 'vld__timestart', 'vld__timeend')
        livetime_dict = SortedDict();
        livetime = 0;
        for value in value_list:
            delta = value['vld__timeend'] - value['vld__timestart']
            livetime += (delta.days + delta.seconds/86400.)
            livetime_dict[value['runno']] = livetime
        xpoints = livetime_dict.keys()
        ypoints = livetime_dict.values()
        nRuns = len(xpoints)
        nPoints = 1000
        step = int(nRuns/nPoints)+1                            
        info['xpoints'] = xpoints[::step]
        info['ypoints'] = ypoints[::step]
        for i in range(len(info['ypoints'])):
            info['ypoints'][i] = float('%.2f' % (info['ypoints'][i], ))
        info['title'] = 'Integrated Up Time (Physics Runs)'
        info['ytitle'] = 'Days'
        info['legend'] = site
    else:
        return HttpResponse(json.dumps({})) # empty
    

                
    return HttpResponse(json.dumps(info))


@login_required
def proxy(request, filename):
    '''proxy to Simon's file service '''
    url = 'http://dayabay.lbl.gov/dybspade/delivery/service/report/docket/' + filename
    import urllib2
    try:
        fh = urllib2.urlopen(url)
    except urllib2.HTTPError:
        return HttpResponse('')
    
    return HttpResponse(fh.read(), content_type="application/xml")
        
