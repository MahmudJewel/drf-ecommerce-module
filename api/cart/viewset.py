from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from api.custompermissions import IsAuthenticatedOrAdmin
from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import CartItemSerializers
from cart.models import Cart, CartItem

# CartItem creation, edition, deletion through viewset
class CartItemViewset(viewsets.ModelViewSet):
    serializer_class = CartItemSerializers
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return cart items associated with the current user's cart
        return self.queryset.filter(cart__user=self.request.user)

