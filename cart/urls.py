from django.urls import path
from . import views

app_name = 'cart'

urlpatterns=[
    path('',views.cart_details,name='cart_details'),
    path('add/<int:product_id>/',views.CartAdd,name='CartAdd'),
    path('remove/<int:product_id>/',views.CartRemove,name='CartRemove'),
]