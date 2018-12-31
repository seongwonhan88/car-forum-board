from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list_view, name='post-list'),
]