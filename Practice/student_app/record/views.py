from django.shortcuts import render, redirect
from .models import Record
from .forms import recordCreate
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf = Record.objects.all()
    return render(request, 'record/student_data.html', {'shelf':shelf})

def upload(request):
    upload = recordCreate()
    if request.method == 'POST':
        upload = recordCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("Your from is not valid")
    else:
        return render(request,'record/upload_form.html', {'upload_form':upload})
    
def update_record(request, record_id):

    print(record_id)
    try:
        record_sel = Record.objects.get(id = record_id)
    except Record.DoesNotExist:
        return redirect('index')
    if request.method == 'POST':
        record_form = recordCreate(request.POST or None, instance = record_sel)
        if record_form.is_valid():
            record_form.save()
            return redirect('index')
        else:
            return HttpResponse("Your from is not valid")
    else:
        return redirect('index')
        
    