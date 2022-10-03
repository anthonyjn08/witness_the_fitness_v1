from django.shortcuts import render
from django.views import generic
from .models import Trainers


class TrainerList(generic.ListView):
    model = Trainers
    queryset = Trainers.objects.all()
    template_name = 'trainers/trainers.html'
    paginate_by = 6
