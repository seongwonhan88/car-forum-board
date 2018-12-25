from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class DomesticCarTalkBoard(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField()
    content = models.TextField()
    is_notification = models.BooleanField(default=False)

    # relational model fields
    tags = models.ManyToManyField('BrandTags', related_name='boards')
    users = models.ManyToManyField('User', related_name='posts')

class BrandTags(models.Model):
    manufacturer = models.CharField(max_length=200)
    brand_logo = models.ImageField(upload_to='logo')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField('User', related_name='comments')


class PostImages(models.Model):
    post_id = models.ForeignKey('DomesticCarTalkBoard')
    image = models.ImageField(upload_to='post')
