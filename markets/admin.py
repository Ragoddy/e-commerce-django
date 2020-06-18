from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin

from markets.models import Category, Telephone, Schedule, Market, Product
from users.models import Client


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'distance', 'sorting', 'image')

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    list_display = ('type_telephone', 'number', 'first', 'market')
    
    
admin.site.register(Schedule)

@admin.register(Market)
class MarketAdmin(OSMGeoAdmin):
    list_display = ('code','name', 'addresses' , 'longitude', 'latitude', 'city','creation_date', 'status', 'telephone_first')
    search_fields = ['name','addresses', 'status']
    ordering = ('-pk',)  
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available', 'status', 'creation_date', 'modification_date', 'market')    
    ordering = ('-creation_date',) 

@admin.register(Client)
class ClientAdmin(OSMGeoAdmin):
    list_display = ('UUID', 'longitude', 'latitude', 'status', 'creation_date')    
    ordering = ('-creation_date',) 
    
    
