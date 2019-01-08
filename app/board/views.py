from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import PostForm
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
        posts = DomesticCarTalkBoard.objects.filter(tags__manufacturer__contains=tag).prefetch_related('tags', 'user')
        if posts:
            context = {
                'posts': posts,
                'tag': tag,
            }
            return render(request, 'board/tag_search_list.html', context)
        return redirect('board:post-detail')


def post_create_view(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            tags = form.cleaned_data['tags']
            post.save()
            if tags:
                for tag in tags:
                    post.tags.add(tag)
            return redirect('board:post-list')
    else:
        form = PostForm()
    context['form'] = form
    return render(request, 'board/post_create.html', context)

