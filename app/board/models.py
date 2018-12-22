from django.db import models

class CarTalkBoard(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField()
    content = models.TextField()


class CarBrands(models.Model):
    pass