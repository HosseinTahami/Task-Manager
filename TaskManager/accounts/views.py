from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm
# Create your views here.

class LoginView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass

class RegisterView(View):
    class_form = CustomUserCreationForm
    template_name = 'register.html'
    def get(self, request):
        form = self.class_form
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')