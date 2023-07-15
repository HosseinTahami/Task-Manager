from django.shortcuts import render
from .models import Category, Tag, Task

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

def task_detail(request):
    return render(request, 'task_detail.html')

def tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': all_tasks})