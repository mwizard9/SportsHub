from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.front,name="front"),
    path('nepal',views.nepal,name="nepal"),
     path('Kids',views.Kids,name="Kids")
    

]
