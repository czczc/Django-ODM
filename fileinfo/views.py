from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list

from odm.fileinfo.models import Daqrawdatafileinfo

import json, os

@login_required
def fileinfo(request, runno):
    '''file info per run'''
        
    file_list = Daqrawdatafileinfo.objects.filter(runno=runno)
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

