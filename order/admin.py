from django.contrib import admin
from .models import Order, OrderItem, DailyData
# Register your models here.

model_list=[Order, OrderItem, DailyData]
admin.site.register(model_list)

