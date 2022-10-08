from django.shortcuts import render,redirect
from .models import *

def blog(request):
    blogs = Blog.objects.all()

    return render(request, 'blog/blog_page.html', {'blogs': blogs})


def blog_d(request, slug):
    post = Blog.objects.filter(slug = slug).first()
    return render(request , 'blog/blog_detail.html' , {'post': post})
