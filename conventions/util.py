# some utility functions from DYB conventions
from datetime import datetime, timedelta        

from odm.conventions.conf import Site, Detector

def DBI_get(objects, context):
    '''
    poor man's DBI filter
    
    Params:
        - objects: a QuerySet object
        - context: a dictionary with 'year', 'month', 'day', 'site', 'detector' defined
    
    Return: the first Query object or None
    '''
    date = datetime(context['year'], context['month'], context['day'])
    if context.get('rollback', ''):
        rollback_date = datetime.datetime(
            context['rollback']['year'], 
            context['rollback']['month'], 
            context['rollback']['day'])
        objects = objects.filter(insertdate__lte=rollback_date)
    
    try:
        # return objects.filter(
        #         timestart__lte=date, 
        #         timeend__gte=date,
        #         subsite=context['detector'],
        #         simmask=1,
        #     ).extra(
        #          where=[ 'sitemask & %s <> 0', ],
        #         params=[ context['site'], ],
        #     ).order_by('-seqno')[0]

        return objects.filter(
                timestart__lte=date, 
                timeend__gte=date,
                subsite=context['detector'],
                simmask=1,
                sitemask=context['site'],
            ).order_by('-seqno')[0]
                    
    except IndexError:
        return None


def DBI_records(objects, site, detector, task, sim, character, width):
    '''
    Format DBI records
    
    Params:
        - objects: the validity table manager
    
    Return: formated output
    '''
    try:
        site = Site.site_id[site]
        detector = Detector.detector_id[detector]
    except KeyError:
        return site + '-' + detector + ' not found.'
    
    values = objects.filter(
        sitemask=site,
        subsite=detector,
        simmask=sim,
        task=task,
    ).values('seqno', 'timestart', 'timeend', 'insertdate')
    
    options = {
        'width' : width,
        'span'  : width+5,
        'character' : character,
    }
    
    output = ''
    fmt_title = "%%7s  %%-19s %%-%ds %%-19s %%s\n" % (options['span'],)
    fmt = "[%%5d]  %%s %%-%ds %%s [%%s]\n" % (options['span'],)    
    output += fmt_title % ('[seqno]', '    valid from', ' ', '    valid to', '    [insert date]')
    output += fmt_title % ('=======', '='*19, ' ', '='*19, '='*21)
    
    timemin = datetime(2038, 1, 20)
    timemax = datetime(1979, 1, 1)
    
    for value in values[::-1]:
        timestart = value['timestart']
        timeend = value['timeend']
        if timestart < timemin: timemin = timestart
        elif timestart > timemax: timemax = timestart
        # days = (timeend - timestart).days
        # if days > 100: days = 100
        # print timestart, '-'*days, timeend
    
    entire_days = (timemax-timemin).days
    scale = entire_days / float(options['width'])
    # print timemin, '--->', timemax, ": ", entire_days, 'days'
    
    for value in values[::-1]:
        timestart = value['timestart']
        timeend = value['timeend']
        pre_width = int((timestart - timemin).days / scale)
        pre = ' ' * pre_width
        if timeend > timemax:  # overflow
            span = options['character'] * (options['span'] - pre_width)
        else:
            span = options['character'] * int((timeend - timestart).days/scale)
                    
        output += fmt % (value['seqno'], timestart, pre+span, timeend, value['insertdate'],)
            
    return output
            