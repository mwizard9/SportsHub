from django.contrib import admin
from.models import Customer, Order, Trend, Nepal, sport,kid

# Register your models here.
admin.site.register(sport)
admin.site.register(Trend)
admin.site.register(Nepal)
admin.site.register(kid)
admin.site.register(Customer)
admin.site.register(Order)