# some utility functions from DYB conventions
import datetime

def DBI_get(objects, context):
    '''
    poor man's DBI filter
    
    Params:
        - objects: a QuerySet object
        - context: a dictionary with 'year', 'month', 'day', 'site', 'detector' defined
    
    Return: the first Query object or None
    '''
    date = datetime.datetime(context['year'], context['month'], context['day'])
    
    try:
        return objects.filter(
                timestart__lte=date, 
                timeend__gte=date,
                subsite__in=[ 0, context['detector'] ],
            ).extra(
                 where=[ 'sitemask & %s <> 0', ],
                params=[ context['site'], ],
            ).order_by('-timestart', '-seqno')[0]
    except IndexError:
        return None
        