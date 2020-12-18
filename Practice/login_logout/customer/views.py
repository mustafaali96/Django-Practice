from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import customer_model
from .forms import customer_form
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.urls.base import reverse
# Create your views here.


def login_view(request):

    if request.user.is_authenticated:
        return render(request, 'customer/index.html')

    else:
        return render(request, '/login/')

    
def tem_view(request):
    return render(request, 'customer/tem.html')

def signup_view(request):
    if request.method == 'POST':
        count = User.objects.count()
        cust_count = customer_model.objects.count()
        cust_rec = customer_model.objects.all()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            return HttpResponse("Your from is not valid")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def home_view(request):
    count = User.objects.count()
    cust_count = customer_model.objects.count()
    cust_rec = customer_model.objects.all()
    return render(request, 'customer/home.html', {
        'count': count, 'cust_count': cust_count, 
        'cust_rec': cust_rec
    })

@login_required
def cust_view(request):
    count = User.objects.count()
    cust_count = customer_model.objects.count()
    cust_rec = customer_model.objects.all()
    return render(request, "customer/index.html", {
        'count': count, 'cust_count': cust_count, 
        'cust_rec': cust_rec
    })

def cust_profile(request):
    usr_name = request.user.username
    print(usr_name)
    if request.method == 'POST':
        form = customer_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse("Your from is not valid")
    else:
        form = customer_form()
    return render(request, 'customer/register.html', {
        'form': form
    })
