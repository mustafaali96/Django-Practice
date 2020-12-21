from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from lms_app.forms import RegisterForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'lms_app/index.html')

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return render(request, 'lms_app/home.html')
    else:
        return render(request, '/login/')

@login_required
def home(request):
    user_name = request.user.username
    role = request.user.email
    print("user role is:", role)

    return render(request, 'lms_app/home.html')