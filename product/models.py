# library 
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from core.models import CommonModel

# Create your models here.


class Product(CommonModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(default="product/product.jpg", upload_to="product")

    def __str__(self):
        return self.title

