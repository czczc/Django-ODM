from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

from odm.pmtinfo.models import Calibpmtspecvld, Cablemapvld, Calibpmtspec, Cablemap
from odm.misc.models import Energyreconvld, Energyrecon

from odm.dbi.forms import DBIRecordsForm, EnergyReconForm, CalibPMTSpecForm, CableMapForm

import json

@login_required
def records(request):
    '''show dbi records with ascii format'''
    output = ''
        
    if request.GET:
        form = DBIRecordsForm(request.GET) # bound form
        if form.is_valid():
            table = form.cleaned_data['table']
            site = form.cleaned_data['site']
            detector = form.cleaned_data['detector']
            task = form.cleaned_data['task']
            sim = form.cleaned_data['sim']
            character = form.cleaned_data['character']
            width = form.cleaned_data['width']
            
            try:
                exec('model = %s' % (table.title()+'vld',))
            except:
                # raise
                output = table + ' does not exist.'
            
            output = model.objects.records(site, detector, task, sim, character, width)
                
        else:
            output = 'form error'
    else:
        form = DBIRecordsForm() # unbound form
    
    return direct_to_template(request, 
        template = 'dbi/records.html',
        extra_context = {
            'form' : form,
            'output' : output,
        })


@login_required
def trend(request, model='EnergyRecon'):
    '''show dbi value as a funtion of time'''
    
    if model == 'EnergyRecon':
        ThisForm = EnergyReconForm
        description = 'Energy Calibration'
    elif model == 'CalibPMTSpec':
        ThisForm = CalibPMTSpecForm
        description = 'PMT Calibration'
    elif model == 'CableMap':
        ThisForm = CableMapForm
        description = 'Cable Map'
    else:
        return HttpResponse(model + ' does not exist.')
        
    if request.is_ajax():
        form = ThisForm(request.POST)
        if form.is_valid():
            site = form.cleaned_data['site']
            detector = form.cleaned_data['detector']
            sim = form.cleaned_data['sim']
            
            if model == 'EnergyRecon':
                task = form.cleaned_data['task']
                manager = Energyrecon.objects
                values = manager.trend(site, detector, task, sim)
            elif model == 'CalibPMTSpec':
                ring = form.cleaned_data['ring']
                column = form.cleaned_data['column']
                in_out = int(form.cleaned_data['in_out'])
                manager = Calibpmtspec.objects
                values = manager.trend(site, detector, ring, column, in_out, 0, sim)
            elif model == 'CableMap':
                ring = form.cleaned_data['ring']
                column = form.cleaned_data['column']
                in_out = int(form.cleaned_data['in_out'])
                manager = Cablemap.objects
                values = manager.trend(site, detector, ring, column, in_out, 0, sim)
                                            
            return HttpResponse(json.dumps(values))
        else:
            return HttpResponse(json.dumps( {
                'errors': form.errors,
            }))
    else:
        form = ThisForm() # unbound form
        return direct_to_template(request, 
            template = 'dbi/trend/'+model+'.html',
            extra_context = {
                'form' : form,
                'model' : model,
                'description' : description,
            })
                 
    