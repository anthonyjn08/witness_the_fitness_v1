from django.urls import path
from . import views

urlpatterns = [
     path('', views.PostList.as_view(), name='blog'),
     path('add_post/', views.add_post, name='add_post'),
     path('edit_post/<slug:slug>', views.EditPost.as_view(),
          name='edit_post'),
     path('delete_post/<slug:slug>', views.DeletePost.as_view(),
          name='delete_post'),
     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
     path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
     path('delete_comment/<int:pk>', views.DeleteComment.as_view(),
          name='delete_comment'),
]
