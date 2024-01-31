from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()