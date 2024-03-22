from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse
import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	AllowAny,
)
from rest_framework import status
from rest_framework import generics

from django.contrib.auth import get_user_model
User = get_user_model()

import json
import urllib.request

from .serializers import (
	UserSerializers,
	ProductSerializers,
	# WeatherSerializers,
	# ProductSerializers
)

from product.models import Product
from .custompermissions import IsSeller, IsSellerOrAdmin


# Create your views here.


# Customer creation, edition, deletion through viewset
class UserViewset(viewsets.ModelViewSet):
	serializer_class = UserSerializers
	queryset = User.objects.all()
	# queryset = Group.objects.get(name="CUSTOMER").user_set.all()

	def get_permissions(self):
		if self.request.method == 'POST':
			self.permission_classes = [AllowAny, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(UserViewset, self).get_permissions()


# Product creation, edition, deletion through viewset
class ProductViewset(viewsets.ModelViewSet):
	serializer_class = ProductSerializers
	queryset = Product.objects.all()
	# queryset = Group.objects.get(name="CUSTOMER").user_set.all()

	def get_permissions(self):
		if self.request.method == 'GET':
			self.permission_classes = [AllowAny, ]
		else:
			self.permission_classes = [IsSellerOrAdmin, ]
		return super(ProductViewset, self).get_permissions()
