from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainerList.as_view(), name='trainers'),
    path('<slug:slug>/', views.TrainerDetail.as_view(), name='trainer_detail'),
]
