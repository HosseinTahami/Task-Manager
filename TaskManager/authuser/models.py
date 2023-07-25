from django.db import models
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("No Email provided")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
