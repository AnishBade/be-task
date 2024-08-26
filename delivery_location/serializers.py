from rest_framework import serializers
from core.models import DeliveryLocation

class DeliveryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryLocation
        fields = ['id', 'address', 'latitude', 'longitude', 'address_type']
