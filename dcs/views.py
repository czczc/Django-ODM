from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required


@login_required
def monitor(request, site):
    '''details of calibration raw parameters'''
    
    return direct_to_template(request, 
        template = 'dcs/monitor.html',
        extra_context = {
            'site' : site,
        })

    
@login_required
def data(request, model, latest_days=30):
    '''json data of the DCS model, within latest_days'''
    from datetime import datetime, timedelta
    latest = datetime.utcnow() - timedelta(days=int(latest_days))
    try:
        exec('from odm.dcs.models import %s as dcsmodel' % (model,))
        keep = 500
        run_list = dcsmodel.objects.filter(date_time__gte=latest)
        count = run_list.count()
        skip = count / keep
        run_list = run_list.extra(where=['id %% %s = 0'], params=[skip])
        
    except ImportError:
        return HttpResponse(model + ' does not exist')
    
    from django.core import serializers
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", run_list))
    else:
        return HttpResponse('<pre>'+ serializers.serialize("json", run_list, indent=4) + '</pre>')
