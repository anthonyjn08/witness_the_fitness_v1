from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from sports.models import Sports


def view_bag(request):
    """ A view that returns the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add specified class to the shopping bag """

    sport = get_object_or_404(Sports, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         (f'Updated {sport.sport_category } '
                          f'quantity to {bag[item_id]}'))

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {sport.sport_category } to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of specified sport in the shopping bag """

    sport = get_object_or_404(Sports, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         (f'Updated {sport.sport_category } '
                          f'quantity to {bag[item_id]}'))
    else:
        bag.pop(item_id)
        messages.success(request,
                         (f'Removed {sport.sport_category } '
                          'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    try:
        sport = get_object_or_404(Sports, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request,
                         (f'Removed {sport.sport_category }'
                          f'from your bag'))

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
