from django.shortcuts import render, redirect

from .models import DomesticCarTalkBoard


def post_list_view(request):
    if request.method == 'GET':
        posts = DomesticCarTalkBoard.objects.all().prefetch_related('tags', 'user')
        context = {
            'posts': posts,
        }
        return render(request, 'board/post_list.html', context)


def post_detail_view(request, pk):
    if request.method == 'GET':
        post = DomesticCarTalkBoard.objects.get(pk=pk)
        post.view_count += 1
        comments = post.comment.all()
        context = {
            'post' : post,
            'comments' : comments,
        }
        return render(request, 'board/post_detail.html', context)


def tag_search_list_view(request, tag):
    if request.method == 'GET':
        post = DomesticCarTalkBoard.objects.filter(tags=tag)
        if post:
            context = {
                'post': post,
            }
            return render(request, 'board/tag_search_list.html', context)
        return redirect('board:post-detail')
