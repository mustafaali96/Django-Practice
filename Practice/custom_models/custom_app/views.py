from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from custom_app.forms import UserForm, recordCreate
from django.contrib.auth.hashers import make_password
from .models import User
from django.conf import settings

# Create your views here.

def index_view(request):
    return render(request, 'custom_app/index.html')

def index_page(request):
    return render(request, 'custom_app/index_page.html')

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

@login_required(login_url=reverse_lazy("login"),)
def home_view(request):
    # context = User.objects.values('role').distinct()
    # print(context)
    # user_name = request.user.username
    # role = request.user.role
    # subject = request.user.subject
    # print("user role is:", role)
    # print("Subjects are: ", subject)
    # print("User id is: ", request.user.id)
    return render(request, 'custom_app/home.html')

@login_required
def update_record(request):
    userInstance = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        record_form = recordCreate(instance=userInstance, data=request.POST)
        if record_form.is_valid():
            record_form.save()
            return redirect('index')
        print(record_form.errors.as_json())
        return render(request, 'custom_app/update.html', {'upload_form':record_form})
        
    record_form = recordCreate(instance=userInstance)
    return render(request, 'custom_app/update.html', {'upload_form':record_form})