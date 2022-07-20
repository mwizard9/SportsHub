from django.contrib import admin
from django.urls import path

from sportshub.views import front
from.import views


urlpatterns = [
    path('',views.frontpage,name="frontpage"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
   
]
