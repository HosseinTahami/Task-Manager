from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:post_id>', views.task_detail, name='task_detail')
    
]