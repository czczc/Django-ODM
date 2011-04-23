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
    if context.get('rollback', ''):
        rollback_date = datetime.datetime(
            context['rollback']['year'], 
            context['rollback']['month'], 
            context['rollback']['day'])
        objects = objects.filter(insertdate__lte=rollback_date)
    
    try:
        return objects.filter(
                timestart__lte=date, 
                timeend__gte=date,
                subsite=context['detector'],
            ).extra(
                 where=[ 'sitemask & %s <> 0', ],
                params=[ context['site'], ],
            ).order_by('-seqno')[0]
    except IndexError:
        return None
        