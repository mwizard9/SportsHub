from django import template

from sportshub.models import sport


register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(sport , cart):
    keys = cart.keys()
    for id in keys:

        if int(id) == sport.id:
            return True

    return False

@register.filter(name='cart_quantity')
def cart_quantity(sport  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == sport.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(sport  , cart):
    return sport.price * cart_quantity(sport , cart)


@register.filter(name='total_cart_price')
def total_cart_price(sports , cart):
    sum = 0 ;
    for p in sports:
        sum += price_total(p , cart)

    return sum
            

    
    
   