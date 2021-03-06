'''Database Cleamer

based on polorus.py 
$Author$
$Revision$
$Date$
'''

import inspect
from lockss import log;
#print ">> ", inspect.getfile(inspect.currentframe())

from django.core.exceptions import ValidationError

from lockssscript import LockssScript 
from lockssview import *; 

class Cleandb(LockssScript):
    ''' clean all db tables '''
                
    def __init__(self, argv0):
        LockssScript.__init__(self, argv0, '$Revision$', {}) 
    
    @staticmethod 
    def cleanList(lst): 
        if lst:
            log.info("clean: %s" % str(lst[0].__class__));
            for e in lst:
                try:
                    e.full_clean(); 
                except ValidationError as err:
                    print "%s.%d.DELETE  %s" % (e.__class__.__name__, e.id, str(err)); 
                    e.delete();

    def process(self):
        log.info("ignoring all parameters; just cleaning out inconsistent entries in db tables"); 
        Cleandb.cleanList(UrlReport.objects.all())
        Cleandb.cleanList( Url.objects.all())
        Cleandb.cleanList( LockssCacheAuId.objects.all())
        Cleandb.cleanList( LockssCacheAuSummary.objects.all() );
        Cleandb.cleanList( LockssCrawlStatus.objects.all() );
        Cleandb.cleanList( UrlReport.objects.all()) 
        Cleandb.cleanList( CacheCommPeer.objects.all()) 

        
