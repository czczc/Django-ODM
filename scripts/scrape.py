#!/usr/bin/env python

from odm.odmrun.scraper import RunScraper, CommentScraper

def scrape_odmrun(dryrun):
    """update odmrun table"""
    rs = RunScraper(7000)
    rs.scrape_basic(dryrun)

def scrape_notes(dryrun):
    """update comment table"""
    cs = CommentScraper(10400)
    cs.scrape_daq_csv(dryrun)
    
def run(argv):
    if 'dryrun' in argv:
        dryrun = True
    else:
        dryrun = False
    
    if 'odmrun' in argv:
        scrape_odmrun(dryrun)
    if 'notes' in argv:
        scrape_notes(dryrun)