from django.shortcuts import render
from .models import Category, Tag, Task
from  datetime import datetime
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    pass
    return render(request, 'search.html')

def task_detail(request, task_id):
    detail = Task.objects.get(id = task_id)
    now = timezone.now()
    if detail.due_date > now :
        remain = 'Ongoing'
    else:
        remain = 'Finished'
    return render(request, 'task_detail.html', {'detail' : detail , 'remain' : remain})

def tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': all_tasks})