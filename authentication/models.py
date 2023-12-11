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
    firstname=models.CharField(max_length=10,unique=True)
    lastname=models.CharField(max_length=10,  unique=True)
    username=None
    phone_number=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    email_is_verified = models.BooleanField(default=False)
    products=models.ForeignKey(Products,on_delete=models.SET_NULL, null=True)
    # products = ArrayField(models.CharField(max_length=15), null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
