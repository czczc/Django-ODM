from django.http import HttpResponse, HttpResponseRedirect, Http404
from odm.production.diagnostics import Diagnostics
import json

def diagnostics_runlist(request):
    '''return list of processed diagnostics runs'''
    if request.is_ajax():
        return HttpResponse(json.dumps(Diagnostics().run_list))
    else:
        raise Http404
        
def diagnostics_run(request, runno):
    '''single run diagnostic info'''
    
    # for debug
    # return HttpResponse('<pre>'+json.dumps(Diagnostics(runno).info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(Diagnostics(runno).info))
    else:
        raise Http404