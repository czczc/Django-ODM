from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

from odm.pmtinfo.models import Calibpmtspecvld, Cablemapvld
from odm.dbi.forms import DBIRecordsForm

@login_required
def dbi_calibpmtspec(request, site, detector, pmtid=None, character='-'):
    '''Retrieve CalibPMTSpec DBI records'''
    
    output = Calibpmtspecvld.objects.pmtspecTrend(site, detector, pmtid, 'txt', character)
    return HttpResponse("<pre>\n"+output+"</pre>")
    

@login_required
def dbi_cablemap(request, site, detector, sensorid=None, character='-'):
    '''Retrieve CableMap DBI records'''
    
    output = Cablemapvld.objects.cablemapTrend(site, detector, sensorid, 'txt', character)
    return HttpResponse("<pre>\n"+output+"</pre>")


@login_required
def records(request):
    '''show dbi records with ascii format'''
    output = ''
        
    if request.GET:
        description = 'Search'
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
         
    