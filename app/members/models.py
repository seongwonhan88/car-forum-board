from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='users')
    nickname = models.CharField(max_length=100, null=True, blank=True)
