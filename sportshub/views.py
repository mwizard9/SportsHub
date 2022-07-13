from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from cart.forms import CartAddProductForm
from.models import sport
from.models import Trend
from.models import Nepal
from.models import kid

# Create your views here.
     

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

def ProductDetail(request, id, slug):
    product = get_object_or_404(sport, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'detail.html',{'product': product,
                              'cart_product_form': cart_product_form})
