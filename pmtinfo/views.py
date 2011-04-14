from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from odm.pmtinfo.models import Feecablemapvld, Calibpmtspecvld

import json

# ======= Diagnostics =======

@login_required
def pmt(request, site, detector, year, month, day, 
        rollback=False, rollback_year='', rollback_month='', rollback_day=''):
    '''Retrieve DBI PMT related info '''
    
    info = {
        'site' : site,
        'detector' : detector,
        'cablemap_vld_from' : '',
        'cablemap_vld_to' : '',
        'cablemap_vld_insert' : '',
        'cablemap_vld_seqno' : '',
        'pmtspec_vld_from' : '',
        'pmtspec_vld_to' : '',
        'pmtspec_vld_insert' : '',
        'pmtspec_vld_seqno' : '',
        'feename_to_id' : {},
        'pmtname_to_id' : {},
        'pmts' : {}
    };
    
    # disable cable map rollback (if need, let me know)
    cablemaps = Feecablemapvld.objects.cablemapSet(site, detector, year, month, day)
    # allow pmt spec rollback
    pmtspecs  = Calibpmtspecvld.objects.pmtspecSet(
        site, detector, year, month, day,
        rollback, rollback_year, rollback_month, rollback_day)

    if cablemaps:
        cablemap_0 = cablemaps.all()[0]
        info['cablemap_vld_from'] = str(cablemap_0.vld.timestart)
        info['cablemap_vld_to'] = str(cablemap_0.vld.timeend)
        info['cablemap_vld_insert'] = str(cablemap_0.vld.insertdate)
        info['cablemap_vld_seqno'] = str(cablemap_0.vld.seqno)
        for cablemap in cablemaps.all():
            info['feename_to_id'][cablemap.feechanneldesc] = cablemap.sensorid
            info['pmtname_to_id'][cablemap.sensordesc] = cablemap.sensorid
            
            pmt = info['pmts'].setdefault(cablemap.sensorid, {})
            # pmt['feename'] = cablemap.feechanneldesc
            # pmt['pmtname'] = cablemap.sensordesc
            
            for key, value in cablemap.unpack().items():
                pmt[key] = value
           
    if pmtspecs:
        pmtspec_0 = pmtspecs.all()[0]
        info['pmtspec_vld_from'] = str(pmtspec_0.vld.timestart)
        info['pmtspec_vld_to'] = str(pmtspec_0.vld.timeend)  
        info['pmtspec_vld_insert'] = str(pmtspec_0.vld.insertdate)  
        info['pmtspec_vld_seqno'] = str(pmtspec_0.vld.seqno)  
        for pmtspec in pmtspecs.all():
            pmt = info['pmts'].setdefault(pmtspec.pmtid, {})
            pmt['spehigh'] = "%.2f" % pmtspec.pmtspehigh
            pmt['spelow'] = "%.2f" % pmtspec.pmtspelow
            pmt['toffset'] = "%.2f" % pmtspec.pmttoffset

    # for debug
    # return HttpResponse('<pre>'+json.dumps(info, indent=4) + '</pre>')
    
    if request.is_ajax():
        return HttpResponse(json.dumps(info))
    else:
        raise Http404