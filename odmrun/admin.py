from django.contrib import admin
from odm.odmrun.models import Run

class RunAdmin(admin.ModelAdmin):
    list_display = ('runno', 'runtype', 'timestart', 'timeend')
    search_fields = ('runno', 'runtype', )
    date_hierarchy = 'timestart'
    
admin.site.register(Run, RunAdmin)
