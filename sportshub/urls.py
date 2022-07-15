from django.contrib import admin
from django.urls import path
from .views import Home
from.import views

urlpatterns = [
    path('',views.front,name="front"),
    path('home',Home.as_view(),name="homepage"),
    path('nepal',views.nepal,name="nepal"),
     path('Kids',views.Kids,name="Kids")
    

]
