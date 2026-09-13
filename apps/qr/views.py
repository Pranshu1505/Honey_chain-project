"""QR Code serializers and views"""
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import QRCode
from .service import QRCodeService


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'batch', 'code_data', 'qr_image', 'scans', 'created_at']
        read_only_fields = ['id', 'scans', 'created_at']


class QRCodeViewSet(viewsets.ModelViewSet):
    serializer_class = QRCodeSerializer
    permission_classes = [IsAuthenticated]
    queryset = QRCode.objects.all()
    
    @action(detail=True, methods=['post'])
    def generate(self, request, pk=None):
        """Generate QR code for a batch"""
        try:
            qr = self.get_object()
            # Generate QR code
            qr_image = QRCodeService.generate_qr_code(
                qr.batch.batch_id,
                {'quantity': qr.batch.total_quantity, 'type': qr.batch.honey_type}
            )
            qr.qr_image = qr_image
            qr.save()
            
            serializer = self.get_serializer(qr)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def scan(self, request, pk=None):
        """Record a QR code scan"""
        qr = self.get_object()
        qr.scans += 1
        qr.save()
        
        serializer = self.get_serializer(qr)
        return Response(serializer.data, status=status.HTTP_200_OK)
