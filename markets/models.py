# -*- coding: UTF8 -*-

from django.db import models
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

#imports lib´s
import os
import uuid


#choices list´s
STATUS_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]

PHONE_CHOICES = [     
    (0,'N/A'),
    (1,'landline'),
    (2,'mobile'),
    (3,'whatsapp'),
]

DAYS_CHOICES = [     
    (0,'N/A'),
    (1,'Lunes'),
    (2,'Martes'),
    (3,'Miercoles'),
    (4,'Jueves'),
    (5,'Viernes'),
    (6,'Sabado'),
    (5,'Domingo'),
    (6,'Todos los días'),
]

#functions util´s
def category_path(instance, filename):     
    UUID = str(uuid.uuid1()).replace("-", "")
    file_extension = os.path.splitext(filename)    
    filename = UUID + str(file_extension[1])
    return 'images/categories/{0}'.format(filename) 

def product_path(instance, filename): 
    UUID = str(uuid.uuid1()).replace("-", "")
    file_extension = os.path.splitext(filename)
    filename = UUID + str(file_extension[1])
    return 'images/products/{0}'.format(filename) 


def market_path(instance, filename): 
    UUID = str(uuid.uuid1()).replace("-", "")
    file_extension = os.path.splitext(filename)
    filename = UUID + str(file_extension[1])
    return 'images/markets/{0}'.format(filename) 

# Classes for models
class Category(models.Model):
    code = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    distance = models.IntegerField(default=3000, blank=True, null=True)
    sorting = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(upload_to=category_path, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    @property
    def count_markets(self):
        count = 0        
        if Market.objects.filter(categories__id = self.id).exists():
            count = Market.objects.filter(categories__id = self.id).count()
        return count

class Telephone(models.Model):
    type_telephone = models.IntegerField(default=1, choices=PHONE_CHOICES)
    number = models.CharField(max_length=150)
    first = models.BooleanField(default=False)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    market = models.ForeignKey("Market", verbose_name="Market", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
    
class Schedule(models.Model):
    day = models.IntegerField(default=1, choices=DAYS_CHOICES)
    start_hour = models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    market = models.ForeignKey("Market", verbose_name="Market", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)

class Market(models.Model):    
    code = models.CharField(max_length=20, unique=True, null=True)
    name = models.CharField(max_length=200)
    addresses = models.CharField(max_length=200)    
    city = models.CharField(max_length=150)
    minimum_price = models.FloatField()
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    location = models.PointField(geography=True, default=Point(-74.05488966864571, 4.71026094566535, srid=4326))
    categories = models.ManyToManyField('Category')
    image = models.ImageField(upload_to=market_path, blank=True, null=True)
    onwer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    @property
    def longitude(self):
        return self.location.x
    
    @property
    def latitude(self):
        return self.location.y
    
    @property
    def telephone_first(self):
        telephone = None        
        if Telephone.objects.filter(market = self.id).exists():
            telephone = Telephone.objects.filter(market = self.id)[0]
        return str(telephone)

    def set_pk(self):
        self.UUID = uuid.uuid4()

    def save(self, *args, **kwargs):
        if self.UUID is None:
            self.set_pk()
            super(Market, self).save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to=product_path, blank=True, null=True)
    available = models.IntegerField(default=1, choices=STATUS_CHOICES)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    market = models.ForeignKey("Market", verbose_name="Market", on_delete=models.CASCADE)
    # product_type = models.ForeignKey("ProductType", verbose_name="ProductType", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return str(self.title)
    


class ProductType(models.Model):
    name = models.CharField(max_length=200)    
    available = models.IntegerField(default=1, choices=STATUS_CHOICES)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)