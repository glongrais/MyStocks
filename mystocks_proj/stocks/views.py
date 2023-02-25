from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import StockHolding
from .serializers import *

@api_view(['GET', 'POST'])
def stocks_list(request):
    if request.method == 'GET':
        data = StockHolding.objects.select_related('stock').all()

        serializer = StockHoldingSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockHoldingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def stocks_detail(request, pk):
    try:
        stock = StockHolding.objects.get(pk=pk)
    except StockHolding.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StockHoldingSerializer(stock, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def transactions_list(request):
    if request.method == 'GET':
        data = Transaction.objects.select_related('stock').all()

        serializer = TransactionSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
