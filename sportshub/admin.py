from django.contrib import admin
from.models import  Category, customer, order,sport

class Adminsport(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(sport, Adminsport)
admin.site.register(Category,AdminCategory)
admin.site.register(customer)
admin.site.register(order)
