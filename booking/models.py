from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Location(models.Model):
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.location


class services(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(max_length=2000,null=True)
    slug = models.SlugField(max_length=1000 , null=True ,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='featured_image/', null=True)


    service_1 = models.CharField(max_length=200,null=True, blank=True)
    price_1 = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.title


class contact(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=2000,null=True)
    phone_no=models.CharField(null=True, max_length=13)
    message=models.TextField(max_length=200,null=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    services_required=models.CharField(max_length=200,null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200,null=True)
    phone_no = models.IntegerField(null=True)
    message=models.TextField(max_length=200,null=True, blank=True)



    def __str__(self):
        return str(self.user)

class UserProfile(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    phone_no = models.IntegerField(null=True)
