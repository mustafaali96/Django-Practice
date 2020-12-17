from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import customer_model
from django.urls import reverse_lazy
# Create your views here.


def login_view(request):

    if request.user.is_authenticated:
        return render(request, 'customer/index.html')

    else:
        return render(request, 'customer/login.html')

    


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'customer/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'customer/signup.html', {
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
    cust_view_list = customer_model.objects.all()
    context = {'cust_view_list': cust_view_list}
    return render(request, "customer/index.html", context)
