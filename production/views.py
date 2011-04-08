from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
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


# =========== general view =========== 

@login_required
def view(request, production):
    '''general view of production plots'''
    from odm.production.forms import SearchPlotsForm, PQMSearchPlotsForm
    
    is_diagnostics = is_simulation = is_pqm = False
    
    if production == 'diagnostics':
        is_diagnostics = True
        SearchForm = SearchPlotsForm
    elif production == 'simulation':
        is_simulation = True
        SearchForm = SearchPlotsForm
    elif production == 'pqm':
        is_pqm = True
        SearchForm = PQMSearchPlotsForm
    else:
        raise Http404
    
    # Validate the form if send though Ajax, otherwise initialize the form
    if request.method == 'POST':
        if request.is_ajax():
            form = SearchForm(request.POST)
            if form.is_valid():
                return HttpResponse(json.dumps(form.cleaned_data))
            else:
                return HttpResponse(json.dumps( {
                    'errors': form.errors,
                }))
        else:
            return HttpResponse('You seem to have disabled JavaScript in your Browser.')
    else:
        form = SearchForm() # An unbound form
    
    # fetch production run list    
    if is_diagnostics:
        diagnostics = Diagnostics()
        diagnostics.fetch_all()
        run_list = diagnostics.run_list.keys()
        title = 'Diagnostic Plots'
        jump_to = '#diagnostics'
    elif is_simulation:
        simulation = Simulation()
        simulation.fetch_all()
        run_list = simulation.run_list.keys()
        title = 'Simulation Plots'
        jump_to = 'sim'
        SearchForm = SearchPlotsForm
    elif is_pqm:
        run_list = Pqm().run_list.keys()
        title = 'PQM Plots'
        jump_to = '#pqm'
    else:
        return HttpResponse("Strange, you shouldn't reach here")

    if not run_list:
        return HttpResponse('<h1>No ' + title + ' Found</h1>')

    from odm.common.util import reversepage_runlist
    paged_runlist = reversepage_runlist(run_list)
    # return HttpResponse('<pre>'+json.dumps(paged_runlist, indent=4) + '</pre>')

    return direct_to_template(request, 
        template = 'production/view.html',
        extra_context = {
            'jump_to' : jump_to,
            'title' : title,
            'paged_runlist' : paged_runlist,
            'form' : form,
        })    
    
@login_required
def search(request, production):
    '''production plots searching result'''
    
    