from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sports, name='sports'),
    path('<int:sport_id>/', views.sport_detail, name='sport_detail'),
    path('add/', views.add_sport, name='add_sport'),
]