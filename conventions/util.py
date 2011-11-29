# some utility functions from DYB conventions
from datetime import datetime, timedelta        

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


def DBI_format(values, format='txt'):
    '''
    Format DBI values to human readable
    
    Params:
        - values: a value list from .values query, must at least contain key 'timestart', 'timeend'
    
    Return: formated output
    '''
    output = "[%-6s %s]\n%s\n" % ('seqno', 'insert date', '=' * 20)
    
    txt_option = {
        'width' : 80,
        'span'  : 90,
        'character' : '|',
    }
    
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
    scale = entire_days / float(txt_option['width'])
    # print timemin, '--->', timemax, ": ", entire_days, 'days'
    
    for value in values[::-1]:
        timestart = value['timestart']
        timeend = value['timeend']
        pre_width = int((timestart - timemin).days / scale)
        pre = ' ' * pre_width
        if timeend > timemax:  # overflow
            span = txt_option['character'] * (txt_option['span'] - pre_width)
        else:
            span = txt_option['character'] * int((timeend - timestart).days/scale)
        
        fmt = "[%%-6d %%s]  %%s %%-%ds %%s\n" % (txt_option['span'],)
            
        output += fmt % (value['seqno'], value['insertdate'], timestart, pre+span, timeend)
    
    print output
        
    return output
            