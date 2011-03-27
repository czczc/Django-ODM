from django.http import HttpResponse, HttpResponseRedirect, Http404
from odm.production.diagnostics import Diagnostics

import json

def diagnostics_runlist(request):
    '''return list of processed diagnostics runs'''
    if request.is_ajax():
        return HttpResponse(json.dumps(Diagnostics('1').run_list))
    else:
        raise Http404