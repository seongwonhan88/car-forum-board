from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list_view, name='post-list'),
    path('<int:pk>/', views.post_detail_view, name='post-detail'),
    path('tag/<str:tag>/', views.tag_search_list_view, name='tag-list'),
    path('create/', views.post_create_view, name='post-create'),
]