# common utilities for all apps

def reversepage_runlist(run_list):
    '''
    make a long runlist paged to thousands and tens
    useful fo template usage
    '''
    run_list = [int(run) for run in run_list]
    run_list.sort(reverse=True)
        
    paged_runlist = []
    index = 0
    for thousand in range(0, run_list[0]/1000+1):
        paged_runlist.append( {} )
        page = paged_runlist[index]
        # page['index'] = thousand
        page['title'] = "%d - %d" % (thousand*1000, (thousand+1)*1000)
        page['thousand'] = thousand
        page['run_tens'] = []
        index += 1
    
    for run in run_list:
        thousand = run / 1000
        paged_runlist[thousand]['run_tens'].append(run)
    
    # break run list into chunks of ten
    chunks = lambda l, n: [l[x: x+n] for x in xrange(0, len(l), n)]
    for paged_run in paged_runlist:
        paged_run['run_tens'] = chunks(paged_run['run_tens'], 10)
    # empty zero-length page
    paged_runlist = [
        paged_run for paged_run in paged_runlist if paged_run['run_tens']
    ]
    # fill in nulls if not up to ten, and 
    for paged_run in paged_runlist:
        for run_tens in paged_run['run_tens']:
            for i in range(10):
                try:
                    run = run_tens[i]
                except IndexError:
                    run_tens.append('')        
    paged_runlist.reverse()
    
    return paged_runlist
    
    