from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import View, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import IntegrityError, transaction

from rest_framework.authtoken.models import Token


import json

#import models
from markets.models import Market, Product, Category, Telephone
from orders.models import Order, ProductByOrder

from markets.forms import ProductForm, MarketForm
from orders.forms import OrderForm

def ReturnMarket(request):
    try:
        market = Market.objects.get(onwer = request.user.id).id
    except Market.DoesNotExist:
        market = 0
    return market

def ReturnToken(request):
    try:
        if Token.objects.filter(user_id = request.user.id).exists():
            token = Token.objects.get(user_id = request.user.id).key
        else:
            token = Token()
            token.user_id = request.user.id
            token.save()
            
            token = token.key
            
    except Token.DoesNotExist:
        token = 0
    return token

class HomeView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):        
        orders_count = 0
        products_count = 0      
        orders_historic_count = 0   
        market_id = ReturnMarket(request)   
        token = ReturnToken(request)        
        name = None
                
        categories = Category.objects.all().order_by('sorting')
        
        if market_id > 0:
            name = Market.objects.get(id=market_id).name
            products_count = Product.objects.filter(market=market_id).count()  
            queryset_order = Order.objects.filter(market=market_id);
            orders_count = queryset_order.exclude(status_order__in=[0,3]).count()        
            orders_historic_count = queryset_order.exclude(status_order__in=[1,2]).count()     
        
        return render(request, 'front_market/home.html', locals())

    @method_decorator(login_required)
    @transaction.atomic
    def post(self, request, *args, **kwargs):     
        market_id = ReturnMarket(request)   
        token = ReturnToken(request)         
        form = MarketForm(request.POST, request.FILES)   
        file = None
        
        try:                  
            
            if form.is_valid():         
                
                """ Create Market """
                category = Category.objects.get(id=int(form.cleaned_data['category']))
                market = Market()
                market.name = form.cleaned_data['name_kyper']
                market.addresses = form.cleaned_data['addresses']
                market.city = form.cleaned_data['city']
                market.minimum_price = form.cleaned_data['minimum_price']
                market.delivery_price = form.cleaned_data['delivery_price']
                market.location = str(form.cleaned_data['location']).split(';')[1]
                market.image = form.cleaned_data['file']
                market.onwer = request.user
                market.save()        
                market.categories.add(category)   
                
                """ Create Phone """
                phone = Telephone()
                phone.type_telephone = 2
                phone.number = form.cleaned_data['number']
                phone.first = 1
                phone.market = market
                phone.save()
            
                return HttpResponseRedirect("/web/markets/products/")
            
            else:
                categories = Category.objects.all().order_by('sorting')
                return render(request, 'front_market/home.html', locals())
            
        except IntegrityError:
            return render(request, 'front_market/home.html', locals())
                      

class ProductView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        request.session['message'] = False
        request.session['saved'] = False        
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)  
        product_exists = False
            
        if market_id > 0:               
            product_exists = Product.objects.filter(market = market_id).exists()
            return render(request, 'front_market/product.html', locals())
        else:
            return HttpResponseRedirect("/web/markets/")
            
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)   
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
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)   
        if market_id > 0:     
            return render(request, 'front_market/order.html', locals())
        else:
            return HttpResponseRedirect("/web/markets/")
    
    
class PromoView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)   
        if market_id > 0:     
            return render(request, 'front_market/promo.html', locals())
        else:
            return HttpResponseRedirect("/web/markets/")
    

class KyperView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)   
        if market_id > 0:     
            market = Market.objects.get(id=market_id)           
            return render(request, 'front_market/kyper.html', locals())
        else:
            return HttpResponseRedirect("/web/markets/")
        


class OrderCreateView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        market_id = ReturnMarket(request) 
        token = ReturnToken(request)   
        name = None        
        
        if market_id > 0:     
            name = Market.objects.get(id=market_id).name
            return render(request, 'front_market/create_order.html', locals())
        else:
            return HttpResponseRedirect("/web/markets/")
        
    
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