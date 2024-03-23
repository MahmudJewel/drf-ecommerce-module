from rest_framework import permissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

class IsSeller(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user and request.user.is_seller:
			return True
		return False

class IsSellerOrAdmin(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user.is_staff or request.user.is_seller:
			return True
		return False

class IsAuthenticatedOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated or request.user.is_staff