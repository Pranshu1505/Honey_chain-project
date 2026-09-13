from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Consumer, Purchase, Review
from .serializers import ConsumerSerializer, PurchaseSerializer, ReviewSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    
    @action(detail=True, methods=['get'])
    def purchase_history(self, request, pk=None):
        """Get consumer purchase history"""
        consumer = self.get_object()
        purchases = Purchase.objects.filter(consumer=consumer)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        """Add review to purchase"""
        purchase = self.get_object()
        Review.objects.get_or_create(purchase=purchase)
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
