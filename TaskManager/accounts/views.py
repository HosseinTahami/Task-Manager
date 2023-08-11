from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class LoginView(View):
    form_class = CustomUserLoginForm
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("TaskApp:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid:
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("TaskApp:home")
        return render(request, self.template_name, {"form": form})


class RegisterView(View):
    class_form = CustomUserCreationForm
    template_name = "register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("TaskApp:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.class_form
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect("TaskApp:home")
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("TaskApp:home")


class ProfileView(View):
    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        return render(request, "profile.html", {"user": user})

    def post(self, request):
        return render(request, "profile.html")
