# library 
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from core.models import CommonModel
from product.models import Product

class Cart(CommonModel):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(CommonModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.title
