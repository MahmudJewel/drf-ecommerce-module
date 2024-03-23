from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

model_list = [Cart, CartItem]
admin.site.register(model_list)
