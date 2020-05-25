# -*- coding: UTF8 -*-

from django.db import models
from markets.models import Market, Product

#imports lib´s
import os
import uuid

#choices

ORDER_CHOICES = [    
    (3,'other'), 
    (2,'web'),
    (1,'android'),
    (0,'ios'),
]

STATUS_ORDER_CHOICES = [     
    (3,'sent'),
    (2,'processing'),
    (1,'received'),
    (0,'cancelled'),
]

PAYMENT_METHOD_CHOICES = [   
    (2,'dataphone'),
    (1,'cash'),
    (0,'none'),
]

STATUS_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]


class Order(models.Model):
    UUID = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    type_so = models.IntegerField(default=1, choices=ORDER_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    market = models.ForeignKey("markets.Market", verbose_name="Market_Order", on_delete=models.CASCADE)
    payment_method = models.IntegerField(default=1, choices=PAYMENT_METHOD_CHOICES)
    status_order = models.IntegerField(default=1, choices=STATUS_ORDER_CHOICES)
    total_price = models.FloatField(default=0)   
    comments = models.TextField(max_length=500, blank=True, null=True)    
    domiciliary = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200) 
    complement_address = models.CharField(max_length=200, blank=True, null=True) 
    name_client = models.CharField(max_length=200) 
    phone = models.CharField(max_length=200, blank=True, null=True) 
    
    def __str__(self):
        return str(self.id)
    

class ProductByOrder(models.Model):
    creation_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    order = models.ForeignKey("Order", verbose_name="Order", on_delete=models.CASCADE)
    product = models.ForeignKey("markets.Product", verbose_name="Product_Order", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)    
    total_price = models.FloatField(default=0)    
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.product.title)
    
    @property
    def product_name(self):
        return self.product.title