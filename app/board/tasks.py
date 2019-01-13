from __future__ import absolute_import
from celery import shared_task


@shared_task
def bring_all_post_list():
    from .models import DomesticCarTalkBoard
    posts = DomesticCarTalkBoard.objects.all().prefetch_related('tags', 'user')
    return posts


@shared_task
def count_up(pk):
    from .models import DomesticCarTalkBoard
    post = DomesticCarTalkBoard.objects.get(pk=pk)
    post_count = post.view_count + 1
    return post_count

