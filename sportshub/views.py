from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from.models import sport
from.models import Trend
from.models import Nepal
from.models import kid
from django.views import View



# Create your views here.
class Cart(View):
    def get(self , request):
        ids=list(request.session.get('cart').keys())
        sports = sport.get_sports_by_id(ids)
        print(sports)
        return render(request , 'cart.html' ,{'sports' : sports})

class Home(View):

    def post(self , request):
        sports = sport.objects.all()
        Trends = Trend.objects.all()
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1

                else:
                    cart[product] = quantity+1

            else:
                cart[product]=1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' ,request.session['cart'])

        return render(request,'home.html',{'sports':sports ,'Trends':Trends})

    def get(self , request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart = {}
        products = None
        request.session.get('cart').clear()


def front(request):
    sports = sport.objects.all()
    Trends = Trend.objects.all()
  

    return render(request,'home.html',{'sports':sports ,'Trends':Trends})

def nepal(request):
    nepals = Nepal.objects.all()

    return render(request,'nepal.html',{'nepals':nepals})


def Kids(request):
    kids = kid.objects.all()
    return render(request,'Kids.html',{'kids':kids})



