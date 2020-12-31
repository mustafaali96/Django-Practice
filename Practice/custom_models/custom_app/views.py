from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from custom_app.forms import UserForm, updateUser, addCourse
from django.contrib.auth.hashers import make_password
from django.contrib.admin.views.decorators import staff_member_required
from custom_app.models import User
from django.conf import settings

# Create your views here.

def index_view(request):
    return render(request, 'custom_app/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            # subjectQuery = form.cleaned_data.get('subject')
            # f_name = form.cleaned_data['first_name']
            # l_name = form.cleaned_data['last_name']
            # u_name = form.cleaned_data['username']
            # make_password(form.cleaned_data['password'])
            # rol = form.cleaned_data['role']
            # img = form.cleaned_data['user_image']
            # objects = User.objects.create(first_name=f_name, last_name=l_name,
            #  username=u_name, password=passwrd, role=rol, user_image=img )
            # for items in subjectQuery.iterator():
            #     print(items)
            #     objects.subject.add(items)
            #     # User.subject.add(items)
            # print("User Form is ", form)
            # print("type of form is: ", allQueryset)
            # print("Your Form Password: ", form.data['password'])
            # password = make_password(form.cleaned_data['password'])
            # form.data['password'] = make_password(form.data['password'])
            # print("your clean pass ", password)
            # print(password1)
            user_form = form.save(commit=False)
            # print("user password: ", user_form.password)
            user_form.password = make_password(user_form.password)
            user_form.save()
            try:
                user_form.save_m2m()
            except Exception:
                pass

            return redirect('login')
        else:
            print(form.errors)
            return render(request, 'registration/signup.html', 
                            {'form': form})
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.user.is_staff:
        return redirect("/admin/")
    elif request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'registration/login.html')

@login_required(login_url=reverse_lazy("login"),)
def home_view(request):
    # context = User.objects.values('role').distinct()
    # user_name = request.user.username
    # role = request.user.role
    # subject = request.user.subject
    if request.user.is_staff:
        return redirect("/admin/")
    else:
        return render(request, 'custom_app/profile.html')

@login_required(login_url=reverse_lazy("login"),)
def update_record(request):
    if request.method == 'POST':
        record_form = updateUser(request.POST,request.FILES, instance=request.user)
        if record_form.is_valid():
            record_form.save()
            try:
                record_form.save_m2m()
            except Exception:
                pass
            return redirect('home')
        return render(request, 'custom_app/update.html', 
                        {'upload_form':record_form})
        
    record_form = updateUser(instance=request.user)
    return render(request, 'custom_app/update.html', 
                    {'upload_form':record_form})

@login_required(login_url=reverse_lazy("login"),)
def record_list(request):
    record = User.objects.all()
    for sub in request.user.subject.all():
        print("your subjects" , sub)
        print(User.objects.filter(subject=sub))
        if request.user.role == 'Teacher':
            record = User.objects.filter(role= 'Student', subject= sub)
        elif request.user.role == 'Student':
            record = User.objects.filter(role= 'Teacher', subject= sub)
        print("Your records are: ", record)
        # for i in record:
        #     print(i.subject.all())
        # print(request.user.user_image)
        return render(request, 'custom_app/records.html',
                        {'record': record})

@login_required(login_url=reverse_lazy("login"),)
def studentsRec_view(request, user_id):
    details = User.objects.get(id=user_id)
    # print(details)
    return render(request, 'custom_app/studentRecord.html',
                            {'details': details})

@staff_member_required(login_url=reverse_lazy("login"),)
def addCourseView(request):
    if request.method == 'POST':
        course_form = addCourse(request.POST)
        if course_form.is_valid():
            course_form.save()
            return redirect('home')
        else:
            return render(request, 'custom_app/addCourse.html', 
                            {'course_form': course_form})
    else:
        course_form = addCourse()
    return render(request, 'custom_app/addCourse.html', {'course_form': course_form})
