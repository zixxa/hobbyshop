from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price= serializers.IntegerField()
