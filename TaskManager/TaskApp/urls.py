from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/',),
    path('tasks/',),
    path('tasks/<int:post_id>',)
    
]