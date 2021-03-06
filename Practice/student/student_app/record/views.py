from django.shortcuts import render
from .models import Record
from .forms import recordCreate
from django.http import HttpResponse
# Create your views here.

def index(request):
    shelf = Record.object.all()
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
    record_id = int(record_id)
    try:
        record_sel = Record.objects.get(id = record_id)
    except Record.DoesNotExist:
        return redirect('index')
    record_form = recordCreate(request.POST or None, instance = record_sel)
    if record_form.is_valid():
        record_form.save()
        return redirect('index')
    return render(request, 'record/upload_form.html', {'upload_form':record_form})
        
    