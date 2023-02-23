from rest_framework import serializers
from .models import Stock, StockHolding, Transaction

# Define a serializer for the Stock model
class StocksSerializer(serializers.ModelSerializer):

    class Meta:
        # Set the model that this serializer will be used to serialize
        model = Stock
        # Specify that all fields on the Stock model should be included in the serialized output
        fields = '__all__'

# Define a serializer for the StockHolding model
class StockHoldingSerializer(serializers.ModelSerializer):

    # Include a nested representation of the related Stock instance in the serialized output
    stock = StocksSerializer(many=False, read_only=True)

    class Meta:
        # Set the model that this serializer will be used to serialize
        model = StockHolding 
        # Specify that all fields on the StockHolding model should be included in the serialized output
        fields = '__all__'
        # Specify that one level of related models should be included in the serialized output
        depth=1

# Define a serializer for the Transaction model
class TransactionSerializer(serializers.ModelSerializer):

    # Include a nested representation of the related Stock instance in the serialized output
    stock = StocksSerializer(many=False, read_only=True)

    class Meta:
        # Set the model that this serializer will be used to serialize
        model = Transaction 
        # Specify that all fields on the Transaction model should be included in the serialized output
        fields = '__all__'
        # Specify that one level of related models should be included in the serialized output
        depth=1
