from django.shortcuts import render,redirect
from .models import *

def products(request):
    items = Products.objects.all()

    return render(request, 'ecom/products_page.html', {'items': items})


def products_d(request, slug):
    product_d = Products.objects.filter(slug = slug).first()
    return render(request , 'ecom/product_detail.html' , {'product_d': product_d})
