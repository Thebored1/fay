from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('booking:home')

    else:
        form = UserCreateForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)





@csrf_exempt
def home(request):
    service = services.objects.all()
    
    query = request.POST.get('content', '')
    category = request.POST.get('category', '')
    
    category_1 = services.objects.filter(category=1).values()
    category_2 = services.objects.filter(category=2).values()
    allPosts= services.objects.filter(title__icontains=query, slug__icontains=query,).values()
    return render(request , 'home.html' ,{'service' : service, 'allPosts': allPosts, 'category_1': category_1, 'category_2': category_2})

def serv(request):
    service = services.objects.all()
    
    return render(request , 'service_list.html' ,{'service' : service})

def serv_d(request, slug):
    service_d = services.objects.filter(slug = slug).first()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.services_required = service_d.title
            note.save()
            form.save()
            return redirect('booking:checkout')
            


    form = BookForm()
    return render(request , 'service_detail.html' , {'service_d': service_d, 'form': form})

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
def orders(request):
    model = book.objects.filter(user=request.user).values()
    print()
    return render(request, 'orders.html', {'order': model})


def search(request):
    query = request.POST.get('content', '')
    allPosts= services.objects.filter(title__icontains=query, slug__icontains=query,).values()
    return render(request, 'search.html', {'allPosts': allPosts})


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')

def legal(request):
    return render(request, 'legal.html')

def terms(request):
    return render(request, 'terms.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')


