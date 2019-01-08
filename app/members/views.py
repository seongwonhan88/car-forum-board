from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import LoginForm, SignupForm, GenerateRandomUserForm
from .tasks import create_random_user

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


def signup_view(request):
    context = {}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board:post-list')
    else:
        form = SignupForm()
    context['form'] = form
    return render(request, 'members/signup.html', context)


class GenerateRandomUserView(FormView):
    template_name = 'members/generate_random_users.html'
    form_class = GenerateRandomUserForm


    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user.delay(total)
        messages.success(self.request, 'Generating users...')
        return redirect('board:post-list')
