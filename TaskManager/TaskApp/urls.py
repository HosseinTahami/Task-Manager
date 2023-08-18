from django.urls import path
from . import views

app_name = "TaskApp"

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("home/", views.Home.as_view(), name="home"),
    path("search/", views.search, name="search"),
    path("tasks/", views.Tasks.as_view(), name="tasks"),
    path("tasks/<int:task_id>", views.TaskDetail.as_view(), name="task_detail"),
    path("search_results/", views.search_results, name="search_results"),
    path("category/", views.category, name="category"),
    path("category/<int:category_id>", views.category_detail, name="category_detail"),
    path("emergency/", views.emergency_tasks, name="em"),
]
