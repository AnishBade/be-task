from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from core.models import DeliveryLocation
from .serializers import DeliveryLocationSerializer
from rest_framework.authentication import TokenAuthentication

class CreateLocationView(generics.CreateAPIView):
    queryset = DeliveryLocation.objects.all()
    serializer_class = DeliveryLocationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveLocationView(generics.ListAPIView):
    serializer_class = DeliveryLocationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DeliveryLocation.objects.filter(user=self.request.user)
