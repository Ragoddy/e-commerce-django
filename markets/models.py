from django.db import models

STATE_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]

PHONE_CHOICES = [     
    (0,'N/A'),
    (1,'landline'),
    (2,'mobile'),
    (3,'whatsapp'),
]

def category_path(instance, filename): 
    print(instance)
	return 'category_{0}/{1}'.format(instance.id, filename) 

def product_path(instance, filename): 
    print(instance)
	return 'product_{0}/{1}'.format(instance.id, filename) 


class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    state = models.IntegerField(default=1, choices=STATE_CHOICES)
    image = models.ImageField(upload_to=category_path, height_field=50, width_field=50, max_length=250, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Telephone(models.Model):
    type_telephone = models.IntegerField(default=1, choices=PHONE_CHOICES)
    number = models.CharField(max_length=150)
    first = models.BooleanField(default=False)
    market = models.ForeignKey("Market", verbose_name="Market", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.type_telephone + " - " + self.number

class Market(models.Model):    
    name = models.CharField(max_length=200)
    addresses = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=150)
    minimun_price = models.FloatField()
    categories = models.ManyToManyField('Category')
    products = models.ManyToManyField('Product')
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True, null=True)
    size = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to=product_path, height_field=50, width_field=50, max_length=250)
    categories = models.ManyToManyField('Category')
    
    def __str__(self):
        return self.name