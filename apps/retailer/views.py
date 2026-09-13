from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Retailer, Product, Sale
from .serializers import RetailerSerializer, ProductSerializer, SaleSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    
    @action(detail=True, methods=['get'])
    def sales_summary(self, request, pk=None):
        """Get retailer sales summary"""
        retailer = self.get_object()
        total_sales = Sale.objects.filter(product__retailer=retailer).count()
        return Response({'total_sales': total_sales})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
