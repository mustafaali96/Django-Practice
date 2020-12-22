from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from custom_app.forms import UserForm
from django.contrib.auth.hashers import make_password

# Create your views here.

def index_view(request):
    return render(request, 'custom_app/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'registration/login.html')

@login_required
def home_view(request):
    user_name = request.user.username
    role = request.user.email
    print("user role is:", role)

    return render(request, 'custom_app/home.html')