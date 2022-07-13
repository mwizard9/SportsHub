from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CartDetail, name='Cart_detail'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
]
