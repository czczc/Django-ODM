from django.contrib import admin
from odm.runinfo.models import Daqruninfo, Daqruninfovld, Daqcalibruninfo, Daqcalibruninfovld

class DaqruninfoAdmin(admin.ModelAdmin):
    list_display = ('runno', 'runtype', 'vld')
    search_fields = ('runno', 'runtype', )
    
class DaqruninfovldAdmin(admin.ModelAdmin):
    list_display = ('seqno', 'timestart', 'timeend', )
    list_filter = ('timestart',)
    date_hierarchy = 'timestart'

class DaqcalibruninfoAdmin(admin.ModelAdmin):
    list_display = ('runno', 'adno', 'zpositiona', 'zpositionb', 'zpositionc', 'lednumber1', 'lednumber2')
    search_fields = ('runno', )

class DaqcalibruninfovldAdmin(admin.ModelAdmin):
    list_display = ('seqno', 'timestart', 'timeend', )
    list_filter = ('timestart',)
    date_hierarchy = 'timestart'
        
admin.site.register(Daqruninfo, DaqruninfoAdmin)
admin.site.register(Daqruninfovld, DaqruninfovldAdmin)
admin.site.register(Daqcalibruninfo, DaqcalibruninfoAdmin)
admin.site.register(Daqcalibruninfovld, DaqcalibruninfovldAdmin)
