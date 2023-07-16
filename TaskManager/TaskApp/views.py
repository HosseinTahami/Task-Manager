from django.shortcuts import render, get_object_or_404
from .models import Task, Tag
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def home(request):
    all_tasks = Task.objects.all()
    return render(
        request,
        'home.html',
        {'tasks': all_tasks}
        )

def search(request):
    return render(
        request,
        'search.html',
        )


def task_detail(request, task_id):
    detail = Task.objects.get(id = task_id)
    now = timezone.now()
    if detail.due_date > now :
        remain = 'Ongoing'
    else:
        remain = 'Finished'
    tags = detail.tags.all()
    return render(
        request,
        'task_detail.html',
        {'detail' : detail,
        'remain' : remain,
        'tags' : tags}
        )
    

def tasks(request):
    all_tasks = Task.objects.all()
    return render(
        request,
        'tasks.html',
        {'tasks': all_tasks}
        )

def search_results(request):
    if request.method == "POST" :
        searched = request.POST['searched']
        tasks = Task.objects.filter(Q(title__icontains=searched) | Q(tags__name__icontains=searched)).distinct()
        print(tasks)
        return render(
            request,
            'search_results.html',
            {'results' : tasks , 
             'searched' : searched}
            )
    else:
        return render(
        request,
        'search_results.html',
        )