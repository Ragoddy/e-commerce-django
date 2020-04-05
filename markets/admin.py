from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin

from markets.models import Category, Telephone, Schedule, Market, Product


admin.site.register(Category)

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('type_telephone', 'number', 'first', 'market')
    
    
admin.site.register(Schedule)

@admin.register(Market)
class MarketAdmin(OSMGeoAdmin):
    list_display = ('name', 'addresses' , 'longitude', 'latitude', 'creation_date')
    

admin.site.register(Product)