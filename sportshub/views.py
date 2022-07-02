from django.http import HttpResponse
from django.shortcuts import render
from.models import sport
from.models import Trend

# Create your views here.
def front(request):
    sports = sport.objects.all()
    Trends = Trend.objects.all()

    return render(request,'home.html',{'sports':sports})

    return render(request,'home.html',{'Trends':Trends})