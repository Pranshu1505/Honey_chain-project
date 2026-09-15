from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def test_open(request):
    return Response({'message': 'This is open, no auth needed!'})


urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('api/test-open/', test_open),
    path('api/auth/', include('apps.auth.urls')),
    path('api/beekeeper/', include('apps.beekeeper.urls')),
    path('api/hive/', include('apps.hive.urls')),
    path('api/harvest/', include('apps.harvest.urls')),
    path('api/batch/', include('apps.batch.urls')),
    path('api/processing/', include('apps.processing.urls')),
    path('api/blockchain/', include('apps.blockchain.urls')),
    path('api/qr/', include('apps.qr.urls')),
    path('api/sensor/', include('apps.sensor.urls')),
    path('api/admin/', include('apps.admin_portal.urls')),
    path('api/distributor/', include('apps.distributor.urls')),
    path('api/retailer/', include('apps.retailer.urls')),
    path('api/consumer/', include('apps.consumer.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/iot/', include('iot.api_routes')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
