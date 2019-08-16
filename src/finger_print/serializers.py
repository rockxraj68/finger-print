from rest_framework import serializers
from .models import Person

class FingerPrintScannerSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = '__all__'
