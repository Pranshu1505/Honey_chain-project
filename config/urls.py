"""
URL Configuration for honey_chain project.
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
