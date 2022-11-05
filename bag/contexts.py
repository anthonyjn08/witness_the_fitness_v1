from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sports.models import Sports

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        sport = get_object_or_404(Sports, pk=item_id)
        total += quantity * sport.sport_cost
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'sport': sport,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
