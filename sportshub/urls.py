from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('front',views.front,name="front")
]
