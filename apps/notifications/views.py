from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification, Alert, NotificationPreference
from .serializers import NotificationSerializer, AlertSerializer, NotificationPreferenceSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def mark_as_read(self, request, pk=None):
        """Mark notification as read"""
        notification = self.get_object()
        from django.utils import timezone
        notification.status = 'read'
        notification.read_at = timezone.now()
        notification.save()
        return Response(self.get_serializer(notification).data)
    
    @action(detail=False, methods=['get'])
    def unread_count(self, request):
        """Get unread notification count"""
        count = Notification.objects.filter(user=request.user, status='unread').count()
        return Response({'unread_count': count})

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    
    @action(detail=False, methods=['get'])
    def active_alerts(self, request):
        """Get active (unresolved) alerts"""
        alerts = Alert.objects.filter(is_resolved=False)
        serializer = self.get_serializer(alerts, many=True)
        return Response(serializer.data)

class NotificationPreferenceViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get', 'post'])
    def my_preferences(self, request):
        """Get or update user notification preferences"""
        preference, created = NotificationPreference.objects.get_or_create(user=request.user)
        
        if request.method == 'POST':
            serializer = NotificationPreferenceSerializer(preference, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        
        serializer = NotificationPreferenceSerializer(preference)
        return Response(serializer.data)
