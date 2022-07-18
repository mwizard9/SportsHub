from django.contrib import admin
from.models import customer, order, Trend, Nepal, sport,kid

# Register your models here.
admin.site.register(sport)
admin.site.register(Trend)
admin.site.register(Nepal)
admin.site.register(kid)
admin.site.register(customer)
admin.site.register(order)