from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sports, name='sports'),
    path('<sport_id>', views.sport_detail, name='sport_detail'),
]