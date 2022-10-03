from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainerList.as_view(), name='trainers'),
]
