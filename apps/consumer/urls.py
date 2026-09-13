from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsumerViewSet, PurchaseViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'reviews', ReviewViewSet)

app_name = 'consumer'
urlpatterns = [
    path('', include(router.urls)),
]
