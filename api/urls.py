from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewset,
)

router = DefaultRouter()
# Account creation, edition, deletions
router.register("auth/user", UserViewset, basename="authuser")
# router.register("auth/vendor", VendorViewset, basename="authvendor")
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
