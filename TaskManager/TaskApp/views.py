from django.shortcuts import render, redirect
from .models import Task, Category, Tag
from accounts.models import CustomUser
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, time
from django.views import View
from .mixins import TodoOwnerRequiredMixin


# Create your views here.
def main_page(request):
    return render(request, "main_page.html")


def home(request):
    all_tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": all_tasks})


def search(request):
    return render(
        request,
        "search.html",
    )


class TaskDetail(TodoOwnerRequiredMixin, View):
    def post(self, request, task_id):
        tag_name = request.POST["name"]
        tag_list = Tag.objects.all()
        tag_list = list(tag_list)
        try:
            Tag.objects.get(name=tag_name)
        except:
            t = Tag.objects.create(name=tag_name)
            t.save()
            my_task = Task.objects.get(id=task_id)
            my_task.tags.add(t)
        return redirect("tasks")

    def get(self, request, task_id):
        detail = Task.objects.get(id=task_id)
        now = timezone.now()
        if detail.due_date > now:
            remain = "Ongoing"
            detail.status = "O"
            detail.save()
        else:
            remain = "Finished"
            detail.status = "F"
            detail.save()
        tags = detail.tags.all()
        return render(
            request,
            "task_detail.html",
            {"detail": detail, "remain": remain, "tags": tags},
        )


class Tasks(TodoOwnerRequiredMixin, View):
    def post(self, request):
        title = request.POST["title"]
        description = request.POST["description"]
        due_date = request.POST["due_date"]
        status = request.POST["status"]
        category = request.POST["category"]
        category = Category.objects.get(name=category)
        tags_list = request.POST.getlist("tags")
        task_file = request.FILES.get("task_file")
        # if not task_file:
        #     default_image_path = os.path.join(settings.MEDIA_ROOT, 'task_default.png')
        #     with open(default_image_path, 'rb') as f:
        #         task_file = File(f, name='task_default.png')
        new_task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            category=category,
            file=task_file,
        )
        for t in tags_list:
            tag_obj = Tag.objects.get(name=t)
            new_task.tags.add(tag_obj)
            new_task.save()

        return redirect("home")

    def get(self, request):
        all_tags = Tag.objects.all()
        all_tasks = Task.objects.all()
        all_category = Category.objects.all()
        return render(
            request,
            "tasks.html",
            {
                "tasks": list(all_tasks),
                "category": all_category,
                "tags": all_tags,
                "status": Task.objects.all(),
            },
        )


def search_results(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        tasks = Task.objects.filter(
            Q(title__icontains=searched) | Q(tags__name__icontains=searched)
        ).distinct()
        print(tasks)
        return render(
            request, "search_results.html", {"results": tasks, "searched": searched}
        )
    else:
        return render(
            request,
            "search_results.html",
        )


def category(request):
    if request.method == "POST":
        cat_name = request.POST["name"]
        cat_file = request.FILES.get("cat_image")
        if cat_file:
            Category.objects.create(name=cat_name, img=cat_file)
            return redirect("category")
        else:
            Category.objects.create(
                name=cat_name,
            )
            return redirect("category")

    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "category.html", {"category": list(categories)})


def category_detail(request, category_id):
    if request.method == "POST":
        if "sub" in request.POST:
            title = request.POST["title"]
            description = request.POST["description"]
            due_date = request.POST["due_date"]
            status = request.POST["status"]
            category = Category.objects.get(id=category_id)
            tags_list = request.POST.getlist("tags")
            if tags_list:
                task_file = request.FILES.get("task_file")
                new_task = Task.objects.create(
                    title=title,
                    description=description,
                    due_date=due_date,
                    status=status,
                    category=category,
                    file=task_file,
                )
                for t in tags_list:
                    tag_obj = Tag.objects.get(name=t)
                    new_task.tags.add(tag_obj)
                    new_task.save()

                return redirect("category")
            else:
                new_task = Task.objects.create(
                    title=title,
                    description=description,
                    due_date=due_date,
                    status=status,
                    category=category,
                )
                for t in tags_list:
                    tag_obj = Tag.objects.get(name=t)
                    new_task.tags.add(tag_obj)
                    new_task.save()
                return redirect("category")

        elif "UPDATE" in request.POST:
            new_name = request.POST.get("new_name")
            new_img = request.FILES.get("new_image")
            print(new_name)
            cat = Category.objects.get(id=category_id)
            cat.name = new_name
            cat.img = new_img
            cat.save()
            return redirect("category")

    if request.method == "GET":
        all_tags = Tag.objects.all()
        all_category = Category.objects.all()
        category_tasks = Task.objects.filter(category__id=category_id)
        c = Category.objects.get(id=category_id)
        return render(
            request,
            "category_detail.html",
            {
                "tasks": list(category_tasks),
                "category": all_category,
                "tags": all_tags,
                "status": Task.objects.all(),
                "my_cat": c,
            },
        )


def emergency_tasks(request):
    tmp = datetime.combine(datetime.now(), time.max)
    tasks = Task.objects.filter(Q(due_date__lt=tmp) & Q(status="O"))
    return render(request, "em.html", {"tasks": tasks})
