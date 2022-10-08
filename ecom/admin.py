from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')

    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True

admin.site.register(Products, ProductsAdmin)
