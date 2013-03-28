#!/usr/bin/env python2
# Thomas Levine, ScraperWiki Limited

'''
Local version of ScraperWiki Utils, documentation here:
https://scraperwiki.com/docs/python/python_help_documentation/
'''

logfd = None # This does something on the hosted version

class Error(Exception):
    """All ScraperWiki exceptions are instances of this class
    (usually via a subclass)."""
    pass

class CPUTimeExceededError(Error):
    """CPU time limit exceeded."""
    pass

from .utils import log, scrape, pdftoxml 
import utils, sqlite

sql = sqlite

