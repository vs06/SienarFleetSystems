'''
Created on 09/06/2015

@author: victor.sousa
'''
from django.contrib import admin
from sienarfleetsys.models import Ship
from django.utils.translation import ugettext_lazy

admin.site.site_title = ugettext_lazy('SienarFleetSystems')
admin.site.site_header = ugettext_lazy('SienarFleetSystems')
admin.site.index_title = ugettext_lazy('SienarFleetSystems')

class ShipAdmin(admin.ModelAdmin):
    search_fields=[]
    list_filter=['nome']
    _fields=['nome']
    list_display = _fields
    list_display_links = list_display
admin.site.register(Ship,ShipAdmin)


