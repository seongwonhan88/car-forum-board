from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DomesticCarTalkBoard(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    content = models.TextField()
    is_notification = models.BooleanField(default=False)

    # relational model fields
    tags = models.ManyToManyField('BrandTags', related_name='boards')
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)


class BrandTags(models.Model):
    manufacturer = models.CharField(max_length=200)
    logo_image = models.ImageField(upload_to='logo')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


class PostImages(models.Model):
    post = models.ForeignKey('DomesticCarTalkBoard', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now=True)
