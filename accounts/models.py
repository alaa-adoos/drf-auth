from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   phone_numer=models.CharField(max_length=20)