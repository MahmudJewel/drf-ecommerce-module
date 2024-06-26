from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewset,
    ProductViewset,
)
from api.cart.viewset import CartItemViewset
from api.order.views import OrderViewSet

router = DefaultRouter()
# Account creation, edition, deletions
router.register("auth/user", UserViewset, basename="authuser")
router.register("product", ProductViewset, basename="product")
router.register("cartitem", CartItemViewset, basename="cartitem")
router.register("order", OrderViewSet, basename="order")
# router.register("weather", WeatherViewset, basename="weather")
# router.register("product", ProductViewset, basename="product")


urlpatterns = [
    # router
    path("", include(router.urls)),
    # # Search product
    # path("search/", ProductSearch.as_view(), name="search"),
    # # suggest product
    # path("recommendation/", ProductRecommendation.as_view(), name="recommendation"),
]
