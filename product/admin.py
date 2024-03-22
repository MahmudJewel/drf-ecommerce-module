from django.contrib import admin
from .models import Product
# Register your models here.

model_list = [Product]
admin.site.register(model_list)
