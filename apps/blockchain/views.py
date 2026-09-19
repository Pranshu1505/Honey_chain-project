"""Blockchain views"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BlockchainTransaction, BlockchainRecord
from apps.batch.models import HoneyBatch
from .serializers import BlockchainTransactionSerializer, BlockchainRecordSerializer
from .service import BlockchainService


class BlockchainTransactionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlockchainTransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BlockchainTransaction.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def by_batch(self, request):
        """Get blockchain history for a specific batch"""
        batch_id = request.query_params.get('batch_id')
        if not batch_id:
            return Response({'error': 'batch_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        transactions = BlockchainTransaction.objects.filter(batch_id=batch_id).order_by('-timestamp')
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)


class BlockchainRecordViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlockchainRecordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return BlockchainRecord.objects.all()
    
    @action(detail=False, methods=['get'])
    def verify(self, request):
        """Verify a honey batch on blockchain"""
        batch_id = request.query_params.get('batch_id')
        if not batch_id:
            return Response({'error': 'batch_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            record = BlockchainRecord.objects.get(batch_id=batch_id)
            serializer = self.get_serializer(record)
            return Response({
                'verified': True,
                'record': serializer.data
            })
        except BlockchainRecord.DoesNotExist:
            return Response({
                'verified': False,
                'error': 'Batch not found on blockchain'
            }, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['post'])
    def record_transaction(self, request):
        """Record a new transaction on blockchain"""
        batch_id = request.data.get('batch_id')
        transaction_type = request.data.get('transaction_type')
        data = request.data.get('data', {})
        
        if not batch_id or not transaction_type:
            return Response(
                {'error': 'batch_id and transaction_type are required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        blockchain_service = BlockchainService()
        block_data = blockchain_service.create_block_data(batch_id, data)
        
        # Create blockchain transaction
        transaction = BlockchainTransaction.objects.create(
            user=request.user,
            batch_id=batch_id,
            transaction_hash=block_data['transaction_hash'],
            transaction_type=transaction_type,
            data=data,
            status='confirmed'
        )
        
        serializer = BlockchainTransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def create_record(self, request):
        """Create a blockchain record for a honey batch automatically"""
        batch_id = request.data.get('batch_id')
        origin = request.data.get('origin', 'Unknown')

        if not batch_id:
            return Response({'error': 'batch_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            batch = HoneyBatch.objects.get(batch_id=batch_id)
        except HoneyBatch.DoesNotExist:
            return Response({'error': f'Batch {batch_id} not found'}, status=status.HTTP_404_NOT_FOUND)

        if BlockchainRecord.objects.filter(batch_id=batch_id).exists():
            return Response({'error': 'Batch already recorded on blockchain'}, status=status.HTTP_400_BAD_REQUEST)

        blockchain_service = BlockchainService()
        block_data = blockchain_service.create_block_data(batch_id, {
            'honey_type': batch.honey_type,
            'quantity': batch.total_quantity,
            'quality_score': batch.quality_score,
        })

        next_block_number = BlockchainRecord.objects.count() + 1

        record = BlockchainRecord.objects.create(
            batch_id=batch_id,
            origin=origin,
            transaction_hash=block_data['transaction_hash'],
            block_number=next_block_number,
            honey_type=batch.honey_type,
            quantity=batch.total_quantity,
            quality_score=batch.quality_score,
        )

        BlockchainTransaction.objects.create(
            user=request.user,
            batch_id=batch_id,
            transaction_hash=block_data['transaction_hash'],
            transaction_type='batch_creation',
            data={'honey_type': batch.honey_type, 'quantity': batch.total_quantity},
            status='confirmed',
            block_number=next_block_number,
        )

        serializer = self.get_serializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
