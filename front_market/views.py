from django.shortcuts import render
from django.views.generic import View, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#import models
from markets.models import Market, Product
from orders.models import Order

class HomeView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):        
        orders_count = 0
        products_count = 0        
        id_market = 794        
        
        products_count = Product.objects.filter(market=id_market).count()
        orders_count = Order.objects.filter(market=id_market).count()
        
        context = {"orders": orders_count, "products": products_count}
        
        return render(request, 'front_market/home.html', context)


class ProductView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'front_market/product.html', context)


class OrderView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'front_market/order.html', context)
    
    
class PromoView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'front_market/promo.html', context)
    

class KyperView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        print(request.user)
        return render(request, 'front_market/kyper.html', context)