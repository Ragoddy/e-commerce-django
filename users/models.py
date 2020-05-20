# -*- coding: UTF8 -*-

from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

#import´s for user
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


#imports lib´s
import os
import uuid

#choices
STATUS_CHOICES = [     
    (1,'active'),
    (0,'inactive'),
]


# Classes for models
class UserManager(BaseUserManager):    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
            last_login=now,
            date_joined=now, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()    

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    

class Client(models.Model):
    UUID = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    location = models.PointField(geography=True, default=Point(-74.05488966864571, 4.71026094566535, srid=4326))
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
    