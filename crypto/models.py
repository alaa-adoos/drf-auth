from django.db import models
from django.contrib.auth import get_user_model

class Crypto(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    desc=models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name