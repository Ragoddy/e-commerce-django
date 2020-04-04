from django.contrib import admin

from markets.models import Category, Telephone, Schedule, Market, Product


admin.site.register(Category)
admin.site.register(Telephone)
admin.site.register(Schedule)
admin.site.register(Market)
admin.site.register(Product)