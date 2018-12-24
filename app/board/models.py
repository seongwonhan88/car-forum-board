from django.db import models

class DomesticCarTalkBoard(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField()
    content = models.TextField()
    tags = models.ManyToManyField('BrandTags', related_name='boards')


class BrandTags(models.Model):
    company = models.CharField(max_length=200)
    brand_logo = models.ImageField(upload_to='logo')
