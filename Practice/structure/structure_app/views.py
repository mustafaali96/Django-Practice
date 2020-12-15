from django.shortcuts import render
from .models import new_structure
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def new_structure_list(request):
    new_list = new_structure.objects.all()
    context = { 'new_list': new_list}
    print(new_list)
    return render(request, 'structure_app/index.html', context)