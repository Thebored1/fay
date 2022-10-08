from django.urls import path
from .views import * 

urlpatterns = [
    path('services/' , serv , name="services"),
    path('services/<slug>' , serv_d , name="services_detail"),
    path('accounts/register/', register, name='register'),
    path('contact/', Contact, name='contact'),
    path('about/', about, name='about'),
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('search/', search, name='search'),
    path('faq/', faq, name='faq'),
    path('legal/', legal, name='legal'),
    path('terms/', terms, name='terms'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),


]