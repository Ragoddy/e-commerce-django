# -*- coding: UTF8 -*-

from django.db import models
from markets.models import Market

#imports lib´s
import os
import uuid

#choices
STATE_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]

ORDER_CHOICES = [    
    (3,'other'), 
    (2,'web'),
    (1,'android'),
    (0,'ios'),
]


class Order(models.Model):
    type_so = models.IntegerField(default=1, choices=ORDER_CHOICES)
    creation_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    number_phone = models.CharField(max_length=150)
    market = models.ForeignKey("markets.Market", verbose_name="Market_Order", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.type_so)