from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RetailerViewSet, ProductViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'retailers', RetailerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'sales', SaleViewSet)

app_name = 'retailer'
urlpatterns = [
    path('', include(router.urls)),
]
