# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet, WalletTransaction, WalletAddress
from .serializers import WalletSerializer, WalletTransactionSerializer, WalletAddressSerializer

class WalletAPIView(APIView):
    """
    API view for wallets
    """
    def get(self, request):
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletTransactionAPIView(APIView):
    """
    API view for wallet transactions
    """
    def get(self, request):
        transactions = WalletTransaction.objects.all()
        serializer = WalletTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WalletTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletAddressAPIView(APIView):
    """
    API view for wallet addresses
    """
    def get(self, request):
        addresses = WalletAddress.objects.all()
        serializer = WalletAddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WalletAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletDetailAPIView(APIView):
    """
    API view for a single wallet
    """
    def get_object(self, pk):
        try:
            return Wallet.objects.get(pk=pk)
        except Wallet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

    def put(self, request, pk):
        wallet = self.get_object(pk)
        serializer = WalletSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wallet = self.get_object(pk)
        wallet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
