from collections import UserList
from unicodedata import category
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
import datetime

from requests import delete

# Create your models here.

class sport(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    @staticmethod
    def get_sports_by_id(ids):
        return sport.objects.filter(id__in =ids)

    def __str__(self):
        return self.name


class Category(models.Model):
     name=models.CharField(max_length=100)
   

class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE,default=1)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if customer.objects.filter(email = self.email):
            return True

        return  False


class order(models.Model):
    sport = models.ForeignKey(sport,
                                on_delete=models.CASCADE)
    customer1 = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer1(user_id):
        return order.objects.filter(customer1 = user_id).order_by('-date')
    



   