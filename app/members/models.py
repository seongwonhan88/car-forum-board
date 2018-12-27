from django.contrib.auth.models import AbstractUser
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='users')
    nickname = models.CharField(max_length=100, null=True, blank=True)

    @property
    def get_image_url(self):
        if self.img_profile:
            return self.img_profile.url
        return static('images/blank_user.png')

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = f'{verbose_name} 목록'
