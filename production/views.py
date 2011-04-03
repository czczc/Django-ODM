from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from odm.production.diagnostics import Diagnostics
from odm.production.pqm import Pqm
from odm.production.simulation import Simulation

import json

# ======= Diagnostics =======

@login_required
def diagnostics_runlist(request):
    '''return list of processed diagnostics runs'''
    
    run = Diagnostics()
    run.fetch_all()
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.run_list))
    else:
        raise Http404

@login_required      
def diagnostics_run(request, runno):
    '''single run diagnostic info'''
    
    run = Diagnostics(runno)
    run.fetch_all()
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(run.info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.info))
    else:
        raise Http404

# ======= Simulation =======

@login_required      
def simulation_run(request, runno):
    '''single run diagnostic info'''
    
    run = Simulation(runno)
    run.fetch_all()
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(run.info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(run.info))
    else:
        raise Http404
        
# =========== PQM ===========

@login_required
def pqm_runlist(request):
    '''return list of processed pqm runs'''    
    if request.is_ajax():
        return HttpResponse(json.dumps(Pqm().run_list))
    else:
        raise Http404
        
@login_required
def pqm_run(request, runno):
    '''single run diagnostic info'''
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(Pqm(runno).info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(Pqm(runno).info))
    else:
        raise Http404
        