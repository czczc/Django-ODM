from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.conf import settings

import json

@login_required
def long(request):
    '''figures for long paper'''
    if settings.SITE_LOCAL:
      json_file = '/Users/chaozhang/Projects/DayaBay/code/share/USDBPLots/figures/index.json'
    elif settings.SITE_NERSC:
      json_file = '/project/projectdirs/dayabay/www/odm_figures/long/figures/index.json'
    else:
      raise Http404

    figures = json.load(open(json_file))
    print figures
    return direct_to_template(request, template='figures/detail.html',
        extra_context={
          'base_url' : 'http://portal.nersc.gov/project/dayabay/odm_figures/long/figures/',
          'figures' : figures,
        }
    )
