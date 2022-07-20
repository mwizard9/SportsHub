from django.contrib import admin
from django.urls import path
from .views import Home
from.import views
from.views import Cart
from.views import CheckOut
from.views import Order
from.middleware.auth import auth_middleware

urlpatterns = [
    path('',views.front,name="front"),
    path('cart',Cart.as_view(),name="cart"),
    path('check-out',CheckOut.as_view(),name="checkout"),
    path('order',auth_middleware(Order.as_view()),name="order"),
    path('home',Home.as_view(),name="home"),
    path('nepal',views.nepal,name="nepal"),
    path('Kids',views.Kids,name="Kids"),
     path('logout',views.logout,name="logout"),
     path('store', views.store , name='store'),

   
    
    

]
