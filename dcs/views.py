from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

from django.core import serializers
import json
from decimal import Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
        
@login_required
def monitor(request, site, category='instrument'):
    '''details of calibration raw parameters'''
    
    template_dict = {
        'EH1_instrument' : 'dcs/eh1_instrument.html',
        'EH1_electronics' : 'dcs/eh1_electronics.html',
    }
    
    return direct_to_template(request, 
        template = template_dict.get(site+'_'+category, 'dcs/monitor.html'),
        extra_context = {
            'site' : site,
            'category' : category,
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
        last_id = run_list[0].id
        run_list = run_list.filter(id__in=xrange(last_id, last_id-count, -skip))
        # run_list = run_list.extra(where=['id %% %s = 0'], params=[skip])
    except IndexError:
        pass
    except:
        return HttpResponse(model + ' does not exist')
    
    from django.core import serializers
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", run_list))
    else:
        return HttpResponse('<pre>'+ serializers.serialize("json", run_list, indent=4) + '</pre>')


@login_required
def fetchone(request, model):
    '''json data of the DCS model, latest record'''
    try:
        exec('from odm.dcs.models import %s as dcsmodel' % (model,))
        record = dcsmodel.objects.all()[0]
    except:
        return HttpResponse(model + ' does not exist or not record')
    
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", [record,]))
    else:
        return HttpResponse('<pre>'+ serializers.serialize("json", [record,], indent=4) + '</pre>')


@login_required
def search(request):
    '''seach dcs db, display the chart'''
    from odm.dcs.forms import DcsForm
        
    if request.is_ajax():
        form = DcsForm(request.POST, auto_id='id_eh1_%s')
        if form.is_valid():
            model = form.cleaned_data['model']
            fields = form.cleaned_data['fields']
            fields += ['date_time']
            keep = 500
            try:
                exec('from odm.dcs.models import %s as dcsmodel' % (model,))
                records = dcsmodel.objects.filter(
                    date_time__gte=form.cleaned_data['date_from'], 
                    date_time__lte=form.cleaned_data['date_to'], 
                )
                if form.cleaned_data['points']:
                    keep = form.cleaned_data['points']
                count = records.count()
                skip = count / keep
                last_id = records[0].id
                records = records.filter(id__in=xrange(last_id, last_id-count, -skip))

            except IndexError:
                return HttpResponse(json.dumps([]))
            except:
                return HttpResponse(model + ' does not exist')
            return HttpResponse(serializers.serialize("json", records, fields=fields))
            
        else:
            return HttpResponse(json.dumps( {
                'errors': form.errors,
            }))
    else:
        form = DcsForm(auto_id='id_eh1_%s') # An unbound form
        return direct_to_template(request, 
            template = 'dcs/search.html',
            extra_context = {
                'form' : form,
            })
    
    
def fields(request, model):
    '''json data of the model fields'''
    try:
        exec('from odm.dcs.models import %s as dcsmodel' % (model,))
        record = [field.name for field in dcsmodel._meta.fields if (field.name != 'id' and field.name != 'date_time')]
        record.sort()
        return HttpResponse(json.dumps(record))
    except ImportError:
        return HttpResponse([])        


    