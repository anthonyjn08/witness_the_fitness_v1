from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('sports'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LaNvxLZJVG6RxGNMnRLqU9BQweZKrHm8AYK3RFoRHEvvkDbIGKl89qVWDSXS8uN9VUFXtEc8DZ4oCi2HsIyNjZk00DWvd1bHU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
