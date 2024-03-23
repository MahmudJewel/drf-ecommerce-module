# library 
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()
# import 
from product.models import Product
from cart.models import Cart, CartItem

# *********** start serializer for cartItem ************
class CartItemSerializers(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
    
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product_id', 'quantity', 'price'] 
        read_only_fields = ['cart'] 

    # price will automatically added when product is created
    def get_price(self, obj):
        return obj.product.price

    # cart will automatically selected 
    def create(self, validated_data):
        # Automatically associate the cart with the authenticated user's cart
        cart = self.context['request'].user.cart
        validated_data['cart'] = cart
        return super().create(validated_data)

