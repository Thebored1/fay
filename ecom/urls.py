from django.urls import path
from .views import * 

urlpatterns = [
    path('' , products , name="products"),
    path('product/<slug>' , products_d , name="products_detail"),
]