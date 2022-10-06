from django.shortcuts import render, get_object_or_404
from .models import Sports


def all_sports(request):

    sports = Sports.objects.all()

    context = {
        'sports': sports
    }

    return render(request, 'sports/sports.html/', context)
