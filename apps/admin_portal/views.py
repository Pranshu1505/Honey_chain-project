"""Admin Portal views"""
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .models import AdminReport, AuditLog
from apps.beekeeper.models import BeekeeperProfile


class AdminReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminReport
        fields = ['id', 'title', 'description', 'report_data', 'created_by', 'created_at']
        read_only_fields = ['id', 'created_at']


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = ['id', 'user', 'action', 'resource_type', 'resource_id', 'details', 'timestamp']
        read_only_fields = ['id', 'timestamp']


class AdminReportViewSet(viewsets.ModelViewSet):
    serializer_class = AdminReportSerializer
    permission_classes = [IsAdminUser]
    queryset = AdminReport.objects.all()


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [IsAdminUser]
    queryset = AuditLog.objects.all()


class AdminDashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get admin dashboard statistics"""
        total_users = User.objects.count()
        total_beekeepers = BeekeeperProfile.objects.count()
        
        from apps.batch.models import HoneyBatch
        total_batches = HoneyBatch.objects.count()
        
        return Response({
            'total_users': total_users,
            'total_beekeepers': total_beekeepers,
            'total_batches': total_batches,
        })
    
    @action(detail=False, methods=['post'])
    def verify_user(self, request):
        """Verify a user"""
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            # Mark user as staff/active
            user.is_active = True
            user.save()
            
            AuditLog.objects.create(
                user=request.user,
                action='approve',
                resource_type='user',
                resource_id=user_id,
                details={'reason': request.data.get('reason', '')}
            )
            
            return Response({'message': 'User verified successfully'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
