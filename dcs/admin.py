from django.contrib import admin
from odm.dcs.models import *

class Ad1LidsensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'ultrasonic_ls', 'ultrasonic_gdls')
    list_filter = ('date_time',)
        
admin.site.register(Ad1Lidsensor, Ad1LidsensorAdmin)
