from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('search_results/', views.search_results, name='search_results'),
    path('category/', views.category, name='category')
    
]