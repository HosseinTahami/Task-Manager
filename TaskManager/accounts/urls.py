from .views import LoginView, RegisterView, LogoutView, ProfileView
from django.urls import path


app_name = "accounts"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:user_id>/", ProfileView.as_view(), name="profile"),
]
