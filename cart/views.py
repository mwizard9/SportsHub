from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from sportshub.models import sport
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def CartAdd(request, sport_id):
    cart = Cart(request)
    product = get_object_or_404(sport, id=sport_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def CartRemove(request, sport_id):
    cart = Cart(request)
    product = get_object_or_404(sport, id=sport_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_details(request):
    cart = Cart(request)
    return render(request,'cart/detail.html',{'cart':cart})
                
