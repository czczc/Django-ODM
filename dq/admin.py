from django.contrib import admin
from odm.dq.models import Dataqualitypmt, Dataqualitypmtvld

class DataqualitypmtAdmin(admin.ModelAdmin):
    list_display = ('runno', 'fileno', 'vld', 'pmtid', 'gain', 'darkrate', 'elecnoiserate', 'preadc')
    search_fields = ('runno', )
    
class DataqualitypmtvldAdmin(admin.ModelAdmin):
    list_display = ('seqno', 'timestart', 'timeend', )
    list_filter = ('timestart',)
    date_hierarchy = 'timestart'
        
admin.site.register(Dataqualitypmt, DataqualitypmtAdmin)
admin.site.register(Dataqualitypmtvld, DataqualitypmtvldAdmin)
