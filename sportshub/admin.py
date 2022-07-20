from django.contrib import admin
from.models import  Category, customer, order,sport

# Register your models here.
admin.site.register(sport)
admin.site.register(Category)
admin.site.register(customer)
admin.site.register(order)
