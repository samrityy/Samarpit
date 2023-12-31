from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import JSONField
from .manager import CustomUserManager
from datetime import datetime, date
from django.contrib.postgres.fields import ArrayField
class Products(models.Model):
    name=models.CharField(max_length=10)
    
class CustomUser(AbstractUser):
    firstname=models.CharField(max_length=10,unique=False)
    lastname=models.CharField(max_length=10,unique=False)
    username=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    products = models.ManyToManyField(Products, blank=True)
    total_price=models.IntegerField(default=0)

    # products = ArrayField(models.CharField(max_length=15), null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
