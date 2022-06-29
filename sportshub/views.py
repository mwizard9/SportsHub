from django.http import HttpResponse
from django.shortcuts import render
from.models import sport

# Create your views here.
def front(request):
    sports = sport.objects.all()

    return render(request,'home.html',{'sports':sports})