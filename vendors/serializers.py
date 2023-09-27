from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Phone number must contain only digits.')
        return value