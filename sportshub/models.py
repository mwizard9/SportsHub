from django.db import models

# Create your models here.

class sport(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Trend(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Nepal(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price = models.IntegerField()

class kid(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price = models.IntegerField()
   