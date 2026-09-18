"""Hive views"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Hive, HiveHealth
from .serializers import HiveSerializer, HiveHealthSerializer


class HiveViewSet(viewsets.ModelViewSet):
    serializer_class = HiveSerializer
    permission_classes = [IsAuthenticated]
    
    # def get_queryset(self):
    #     return Hive.objects.filter(apiary__beekeeper=self.request.user)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Hive.objects.all()
        return Hive.objects.filter(apiary__beekeeper=user)
    
    @action(detail=True, methods=['get', 'put'])
    def health(self, request, pk=None):
        try:
            hive = self.get_object()
            health = HiveHealth.objects.get(hive=hive)
        except HiveHealth.DoesNotExist:
            return Response({'error': 'Health metrics not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = HiveHealthSerializer(health)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = HiveHealthSerializer(health, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
