# library 
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from core.models import CommonModel
from product.models import Product

class Order(CommonModel):
    status_list=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
            ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_list, default='pending') 

    def __str__(self):
        return f"{self.user.username}'s order. total price {self.total_price}"

class OrderItem(CommonModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.order.user.username}'s order item {self.product.title}. quantity={self.quantity}"


# daily revenue
class DailyData(CommonModel):
    date = models.DateField(unique=True)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date}'s revenue {self.total_revenue}"

