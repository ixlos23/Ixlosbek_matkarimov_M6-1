from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='')
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)