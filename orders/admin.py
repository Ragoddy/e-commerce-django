from django.contrib import admin

from orders.models import Order, ProductByOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('type_so', 'creation_date', 'market')    
