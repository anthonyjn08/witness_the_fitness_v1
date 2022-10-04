from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]