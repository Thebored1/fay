from django.urls import path
from .views import * 

urlpatterns = [
    path('' , blog , name="blog"),
    path('blog/<slug>' , blog_d , name="blog_detail"),
]