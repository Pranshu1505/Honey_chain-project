"""Processing serializers and views"""
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Processing, QualityTest


class ProcessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processing
        fields = ['id', 'batch', 'temperature', 'duration', 'notes', 'completed_at']
        read_only_fields = ['id']


class QualityTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityTest
        fields = ['id', 'batch', 'acidity', 'moisture', 'color_intensity', 'aroma_grade', 'is_approved', 'test_date']
        read_only_fields = ['id']


class ProcessingViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Processing.objects.all()


class QualityTestViewSet(viewsets.ModelViewSet):
    serializer_class = QualityTestSerializer
    permission_classes = [IsAuthenticated]
    queryset = QualityTest.objects.all()
