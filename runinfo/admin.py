from django.contrib import admin
from odm.runinfo.models import Daqruninfo, Daqruninfovld, Daqcalibruninfo

class DaqruninfoAdmin(admin.ModelAdmin):
    list_display = ('runno', 'runtype', 'vld')
    search_fields = ('runno', 'runtype', )
    
class DaqruninfovldAdmin(admin.ModelAdmin):
    list_display = ('seqno', 'timestart', 'timeend', )
    list_filter = ('timestart',)
    date_hierarchy = 'timestart'

class DaqcalibruninfoAdmin(admin.ModelAdmin):
    list_display = ('runno', 'adno', 'zpositiona', 'zpositionb', 'zpositionc',)
    search_fields = ('runno', )
    
admin.site.register(Daqruninfo, DaqruninfoAdmin)
admin.site.register(Daqruninfovld, DaqruninfovldAdmin)
admin.site.register(Daqcalibruninfo, DaqcalibruninfoAdmin)
