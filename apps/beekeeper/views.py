"""Beekeeper views"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Apiary, BeekeeperProfile
from .serializers import ApiarySerializer, BeekeeperProfileSerializer


class ApiaryViewSet(viewsets.ModelViewSet):
    serializer_class = ApiarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Apiary.objects.filter(beekeeper=self.request.user)

    def perform_create(self, serializer):
        serializer.save(beekeeper=self.request.user)


class BeekeeperProfileViewSet(viewsets.ModelViewSet):
    queryset = BeekeeperProfile.objects.all()
    serializer_class = BeekeeperProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get', 'put'])
    def me(self, request):
        try:
            profile = BeekeeperProfile.objects.get(user=request.user)
        except BeekeeperProfile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BeekeeperProfileSerializer(profile)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = BeekeeperProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
