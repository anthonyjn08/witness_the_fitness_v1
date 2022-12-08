from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Sports
from .forms import SportForm


def all_sports(request):
    """ A view to show all classes and searches """

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
    """ A view to show the detail of each class type """
    
    sport = get_object_or_404(Sports, pk=sport_id)

    context = {
        'sport': sport,
    }

    return render(request, 'sports/sport_detail.html', context)


def add_sport(request):
    """ Add sports to the store """
    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES)
        if form.is_valid():
            sport = form.save()
            messages.success(request, 'Successfully added Sport')
            return redirect(reverse('sport_detail', args=[sport.id]))
        else:
            messages.error(request, 'Failed to add sport. Please make sure the form is valid')
    else:
        form = SportForm()
    template = 'sports/add_sport.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_sport(request, sport_id):
    """ Edit a sport """
    sport = get_object_or_404(Sports, pk=sport_id)
    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES, instance=sport)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated sport')
            return redirect(reverse('sport_detail', args=[sport.id]))
        else:
            messages.error(request, 'Failed to update sport. Please ensure the form is valid')
    else:
        form = SportForm(instance=sport)
        messages.info(request, f'You are editing {sport.sport_category}')

    template = 'sports/edit_sport.html'
    context = {
        'form': form,
        'sport': sport,
    }

    return render(request, template, context)


def delete_sport(request, sport_id):
    """ Delete a sport """
    sport = get_object_or_404(Sports, pk=sport_id)
    sport.delete()
    messages.success(request, 'Sport deleted!')
    return redirect(reverse('sports'))
