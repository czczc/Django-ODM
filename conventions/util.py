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
        rollback_date = datetime(
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
            ).order_by('-versiondate', '-seqno')[0]

    except IndexError:
        return None


def DBI_records(objects, fk, site, detector, task, sim, character, width):
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

    from django.db.models import Count
    values = objects.filter(
        sitemask=site,
        subsite=detector,
        simmask=sim,
        task=task,
    ).values('seqno', 'timestart', 'timeend', 'insertdate', 'versiondate'
    ).order_by('-versiondate', '-seqno'
    ).annotate(count=Count(fk))

    options = {
        'width' : width,
        'span'  : width+5,
        'character' : character,
    }

    output = ''
    fmt_title = "%%7s  %%-19s %%-%ds %%-19s %%5s %%s %%s\n" % (options['span'],)
    fmt = "[%%5d]  %%s %%-%ds %%s %%4d  [%%s] [%%s]\n" % (options['span'],)
    output += fmt_title % ('[seqno]', '    valid from', ' ', '    valid to', 'count', '    [insert date]', '       [version date]')
    output += fmt_title % ('=======', '='*19, ' ', '='*19, '=====', '='*21, '='*21)

    timemin = datetime(2038, 1, 20)
    timemax = datetime(1979, 1, 1)

    for value in values[::-1]:
        timestart = value['timestart']
        timeend = value['timeend']
        if timestart < timemin: timemin = timestart
        if timestart > timemax: timemax = timestart
        if timemin == timemax: timemax = timemin + timedelta(days=10) # only one record

    # print timemax, timemin
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

        output += fmt % (value['seqno'], timestart, pre+span, timeend, value['count'], value['insertdate'], value['versiondate'])

        # print value['count']

    return output


def DBI_trend(objects, site, detector, task, sim):
    '''
    Retrieve correct DBI records as a function of time

    Params:
        - objects: a QuerySet

    Return: a dictionary of DBI records keyed by timestart
    '''
    if not objects:
        return {}

    try:
        site = Site.site_id[site]
        detector = Detector.detector_id[detector]
    except KeyError:
        return {}

    records = objects.filter(
        vld__sitemask=site,
        vld__subsite=detector,
        vld__simmask=sim,
        vld__task=task,
    ).order_by('-vld__versiondate')
    # ).order_by('-vld__seqno')

    if not records:
        return {}

    first = records[0]
    dbi_records = {
        first.vld.timestart : {
            'record' : first,
            'end' : first.vld.timeend,
        }
    }
    uncovered_periods = [
        (datetime(1979, 1, 1), first.vld.timestart),
        (first.vld.timeend, datetime(2038, 1, 20))
    ]

    for record in records[1:]:
        uncovered_periods = check_overlap(record, dbi_records, uncovered_periods)

    return dbi_records


def check_overlap(record, dbi_records, uncovered_periods):

    x = record.vld.timestart
    y = record.vld.timeend

    new_uncovered_periods = []
    for uncovered_period in uncovered_periods:
        a, b = uncovered_period
        if x>=b or y<=a:
            #        a ------ b
            # x ---- y        x ---- y
            # already covered, no action
            new_uncovered_periods.append(uncovered_period)
        else:
            if x<=a and y>=b:
                #    a ------ b
                # x ------------ y
                # covers all, add record
                dbi_records[a] = {'record': record, 'end': b}
            elif x <= a <= y:
                #    a -------- b
                # x ---- y
                # covers early portion, add record
                dbi_records[a] = {'record': record, 'end': y}
                new_uncovered_periods.append( (y, b) )
            elif x <= b <= y:
                # a -------- b
                #        x ---- y
                # covers late portion, add record
                dbi_records[x] = {'record': record, 'end': b}
                new_uncovered_periods.append( (a, x) )
            elif x > a and y < b:
                # a ------------ b
                #     x ---- y
                # covers mid portion, add record
                dbi_records[x] = {'record': record, 'end': y}
                new_uncovered_periods += [ (a, x), (y, b) ]
    # print new_uncovered_periods
    return new_uncovered_periods
