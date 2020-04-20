from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin

from markets.models import Category, Telephone, Schedule, Market, Product
from users.models import Client
from orders.models import Order


admin.site.register(Category)

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('type_telephone', 'number', 'first', 'market')
    
    
admin.site.register(Schedule)

@admin.register(Market)
class MarketAdmin(OSMGeoAdmin):
    list_display = ('name', 'addresses' , 'longitude', 'latitude', 'creation_date', 'state')
    search_fields = ['name','addresses', 'state']
    
admin.site.register(Product)

@admin.register(Client)
class ClientAdmin(OSMGeoAdmin):
    list_display = ('UUID', 'longitude', 'latitude', 'state', 'creation_date')    
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('type_so', 'creation_date', 'number_phone', 'market')