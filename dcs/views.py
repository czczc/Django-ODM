from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail
from django.conf import settings

@login_required
def monitor(request, site):
    '''details of calibration raw parameters'''
    
    return direct_to_template(request, 
        template = 'dcs/monitor.html',
        extra_context = {
            'site' : site,
        })

    
@login_required
def data(request, model):
    '''json data of the DCS model'''

    try:
        exec('from odm.dcs.models import %s as dcsmodel' % (model,))
        run_list = dcsmodel.objects.all()[:100]
    except:
        return HttpResponse(model + ' does not exist')
    
    from django.core import serializers
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", run_list))
    else:
        return HttpResponse('<pre>'+ serializers.serialize("json", run_list, indent=4) + '</pre>')
                
    # if request.is_ajax():
    #     return HttpResponse(json.dumps(info))
    # else:
    #     return HttpResponse('<pre>'+ json.dumps(info, indent=4) + '</pre>')