from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistributorViewSet, ShipmentViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'distributors', DistributorViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'inventory', InventoryViewSet)

app_name = 'distributor'
urlpatterns = [
    path('', include(router.urls)),
]
