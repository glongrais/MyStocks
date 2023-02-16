from rest_framework import serializers
from .models import Stock

class StocksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock 
        fields = ('pk', 'symbol', 'name', 'currentPrice', 'previousClose', 'sector', 'dividendYield', 'logoUrl')