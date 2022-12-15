from django.urls import path
from . import views

urlpatterns = [
    path('', views.SponsorList.as_view(), name='sponsors'),
]