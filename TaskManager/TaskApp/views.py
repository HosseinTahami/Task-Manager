from django.shortcuts import render
from .models import Task, Category
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, time

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
        detail.status = 'O'
        detail.save()
    else:
        remain = 'Finished'
        detail.status = 'F'
        detail.save()
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
        {'tasks': list(all_tasks)}
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

def category(request):
    categories = Category.objects.all()
    return render(
        request,
        'category.html',
        {'category' : list(categories)})

def category_detail(request, category_id):
    category_tasks = Task.objects.filter(category__id=category_id)
    print(category_tasks)
    print(list(category_tasks))
    return render(
        request,
        'category_detail.html',
        {'tasks': list(category_tasks)}
        )

def emergency_tasks(request):
    tmp = datetime.combine(datetime.now(), time.max)
    tasks = Task.objects.filter(Q(due_date__lt=tmp) & Q(status='O'))
    return render(request, 'em.html', {'tasks':tasks})