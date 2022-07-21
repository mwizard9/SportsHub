from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from .models import sport

from.models import order
from django.views import View
from .models import customer
from.models import sport
from.models import Category
from django.contrib.auth.models import User, auth



# Create your views here.
class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        sports = sport.get_sports_by_id(ids)
        print(sports)
        return render(request , 'cart.html' ,{'sports' : sports})



class Home(View):

    def post(self , request):
        sports = sport.objects.all()
        
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

        sports = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            sports = sport.get_all_sports_by_categoryid(categoryID)
        else:
            sports = sport.get_all_sports()

        data = {}
        data['sports'] = sports
        data['categories'] = categories
        return render(request, 'home.html' , data)

        return render(request,'home.html',{'sports':sports })

    def get(self , request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart = {}
        

        
        sports = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            sports = sport.get_all_sports_by_categoryid(categoryID)
        else:
            sports = sport.get_all_sports()

        data = {}
        data['sports'] = sports
        data['categories'] = categories
        return render(request, 'home.html' , data)


 

class CheckOut(View):
    def post(self , request):
        
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer2 = request.user
        
        cart= request.session.get('cart')
        sports = sport.get_sports_by_id(list(cart.keys()))
        
        print(address ,phone , customer , cart , sports)


        for Sport in sports:
            
            Order = order(customer1=customer2,
                          sport=Sport,
                          price=Sport.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(Sport.id)))

            Order.save()

        request.session['cart']={}



            


        return redirect('cart')

class Order(View):
    def get(self , request):
        customer2 = request.user
        Orders=order.get_orders_by_customer1(customer2)
        print(Orders)
        return render(request , 'order.html' , {'orders' : Orders})


def front(request):
    sports = sport.objects.all()
    sports = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        sports = sport.get_all_sports_by_categoryid(categoryID)
    else:
        sports = sport.get_all_sports()

    data = {}
    data['sports'] = sports
    data['categories'] = categories
    return render(request, 'home.html' , data)

   
  

    

def nepal(request):
    

    return render(request,'nepal.html')


def Kids(request):
    
    return render(request,'Kids.html')


def logout(request):
    auth.logout(request)
    return redirect("/")







