from django.contrib import admin

from .models import DomesticCarTalkBoard, BrandTags, Comment, PostImages

admin.site.register(DomesticCarTalkBoard)
admin.site.register(BrandTags)
admin.site.register(Comment)
admin.site.register(PostImages)
