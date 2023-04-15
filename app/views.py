from django.http import HttpResponse
#from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
#from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    return render(request, 'index.html')