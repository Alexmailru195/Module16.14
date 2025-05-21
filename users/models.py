from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Уникальный email
    is_active = models.BooleanField(default=False)  # Временно неактивный пользователь

    def __str__(self):
        return self.username