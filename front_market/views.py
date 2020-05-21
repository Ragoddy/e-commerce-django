from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import View, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import transaction
import json

#import models
from markets.models import Market, Product
from orders.models import Order, ProductByOrder

from markets.forms import ProductForm
from orders.forms import OrderForm

def ReturnMarket(request):
    try:
        market = Market.objects.get(onwer = request.user.id).id
    except Market.DoesNotExist:
        market = 0
    return market

class HomeView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):        
        orders_count = 0
        products_count = 0        
        market_id = ReturnMarket(request)          
        
        name = Market.objects.get(id=market_id).name
        products_count = Product.objects.filter(market=market_id).count()
        orders_count = Order.objects.filter(market=market_id).count()
        
        context = {"orders": orders_count, "products": products_count, "name": name, "market_id": market_id}
        
        return render(request, 'front_market/home.html', context)


class ProductView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        request.session['message'] = False
        request.session['saved'] = False        
        market_id = ReturnMarket(request)        
        return render(request, 'front_market/product.html', locals())
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        market_id = ReturnMarket(request) 
        request.session['message'] = True        
        stock = 0
        data = request.POST        
        form = ProductForm(request.POST, request.FILES)        
        
        if "stock" in request.POST:
            stock = 1
        
        if form.is_valid():            
            market = Market.objects.get(pk = market_id)
            product = Product()
            product.title = form.cleaned_data['title']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.available = stock
            product.image = form.cleaned_data['file']
            product.market = market
            product.save()        
            
            request.session['saved'] = True
            return HttpResponseRedirect(request.path, locals())
        else:
            form = ProductForm()
            request.session['saved'] = False
        return render(request, 'front_market/product.html', locals())
    

class OrderHistoricView(View):
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
        market_id = ReturnMarket(request) 
        market = Market.objects.get(id=market_id)
        return render(request, 'front_market/kyper.html', locals())


class OrderCreateView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        market_id = ReturnMarket(request)         
        name = Market.objects.get(id=market_id).name
        return render(request, 'front_market/create_order.html', locals())
    
    @method_decorator(login_required)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        market_id = ReturnMarket(request)
        total_price = 0
        products = []
        data = request.POST        
        form = OrderForm(request.POST)    
           
        if "products" in request.POST:  
            for prod in data['products'].split(','):
                print(prod)
                price = Product.objects.get(pk=prod).price
                if total_price == 0:
                    total_price = price
                else:
                    total_price = total_price + price                
                
        if form.is_valid():       
            market = Market.objects.get(pk = market_id)
            order = Order()
            order.type_so = 2
            order.market = market
            order.payment_method = form.cleaned_data['payment_method']
            order.total_price = total_price 
            order.comments = form.cleaned_data['comments']
            order.address = form.cleaned_data['address']
            order.complement_address = form.cleaned_data['complement_address']
            order.name_client = form.cleaned_data['name_client']
            order.phone = form.cleaned_data['phone']
            order.save()        
            
            if "products" in request.POST:
                for prod in data['products'].split(','):
                    product = Product.objects.get(pk=prod)
                    pbo = ProductByOrder()
                    pbo.order = order
                    pbo.product = product
                    pbo.amount = 1
                    pbo.unit_price = product.price   
                    pbo.total_price = product.price 
                    pbo.save()
                    
            # request.session['saved'] = True
            # return HttpResponseRedirect(request.path, locals())
        else:
            form = OrderForm()
        return HttpResponseRedirect("/web/markets/")