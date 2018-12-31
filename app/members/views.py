from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('board:post-list')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'members/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('board:post-list')
    else:
        pass
