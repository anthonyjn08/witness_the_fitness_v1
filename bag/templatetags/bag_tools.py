from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(sport_cost, quantity):
    return sport_cost * quantity