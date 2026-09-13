from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Distributor, Shipment, Inventory
from .serializers import DistributorSerializer, ShipmentSerializer, InventorySerializer

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    
    @action(detail=True, methods=['get'])
    def inventory(self, request, pk=None):
        """Get distributor inventory"""
        distributor = self.get_object()
        inventory = Inventory.objects.filter(distributor=distributor)
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    @action(detail=True, methods=['patch'])
    def mark_delivered(self, request, pk=None):
        """Mark shipment as delivered"""
        shipment = self.get_object()
        shipment.status = 'delivered'
        from django.utils import timezone
        shipment.actual_delivery = timezone.now()
        shipment.save()
        serializer = self.get_serializer(shipment)
        return Response(serializer.data)

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
