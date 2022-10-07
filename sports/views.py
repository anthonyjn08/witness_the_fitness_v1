from django.shortcuts import render, get_object_or_404
from .models import Sports


def all_sports(request):
    """ A view to show all sports """
    sports = Sports.objects.all()

    context = {
        'sports': sports
    }

    return render(request, 'sports/sports.html/', context)


def sport_detail(request, sport_id):
    """ A view to show each class type """
    
    sport = get_object_or_404(Sports, pk=sport_id)

    context = {
        'sport': sport
    }

    return render(request, 'sports/sport_detail.html', context)
