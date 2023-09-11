from .models import Task
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied


class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            todo = Task.objects.get(id=kwargs["todo_id"])
            if not todo.user == request.user:
                raise PermissionDenied
            else:
                self.todos = Task.objects.filter(user=request.user)
            return super().dispatch(request, *args, **kwargs)
