# -*- coding: UTF8 -*-

from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

#imports lib´s
import os
import uuid

#choices
STATUS_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]


# Classes for models
class Client(models.Model):
    UUID = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    location = models.PointField(geography=True, default=Point(-74.05488966864571, 4.71026094566535))
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now=True, blank=True, null=True)        

    def __str__(self):
        return str(self.UUID)
    
    @property
    def longitude(self):
        return self.location.x
    
    @property
    def latitude(self):
        return self.location.y


# class Kyper(models.Model):
#     location =models.PointField(geography=True, default=Point(-74.05488966864571, 4.71026094566535))
#     state = models.IntegerField(default=1, choices=STATE_CHOICES)
#     creation_date = models.DateTimeField(auto_now=True, blank=True, null=True)    