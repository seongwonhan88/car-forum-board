from django.shortcuts import render

from .models import DomesticCarTalkBoard


def post_list_view(request):
    if request.method == 'GET':
        posts = DomesticCarTalkBoard.objects.all().prefetch_related('tags', 'posts')
        context = {
            'posts': posts,
        }
        return render(request, 'board/post_list.html', context)