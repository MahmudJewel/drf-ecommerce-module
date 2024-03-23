from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from order.models import Order, OrderItem
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):   
        cart = request.user.cart 
        if cart.cartitem_set.exists():
            cart_items = cart.cartitem_set.all() 
            total_price = 0

            # Create the order
            order = Order.objects.create(user=request.user)
        
            # Create order items and calculate total price
            for cart_item in cart_items:
                total_price += (cart_item.product.price *cart_item.quantity )
                OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.product.price)

             # Set the total price for the order
            order.total_price = total_price
            order.save()

            # Empty the cart
            cart.cartitem_set.all().delete()
            return Response({'message': 'Order placed successfully'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error': 'Cart is empty. Please add items to the cart before placing an order'}, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
