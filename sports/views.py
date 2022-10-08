from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Sports


def all_sports(request):
    """ A view to show all sports """

    sports = Sports.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('sports'))
            
            queries = Q(sport_category__icontains=query) | Q(sport_description__icontains=query)
            sports = sports.filter(queries)

    context = {
        'sports': sports,
        'search_term': query,
    }

    return render(request, 'sports/sports.html/', context)


def sport_detail(request, sport_id):
    """ A view to show each class type """
    
    sport = get_object_or_404(Sports, pk=sport_id)

    context = {
        'sport': sport
    }

    return render(request, 'sports/sport_detail.html', context)
