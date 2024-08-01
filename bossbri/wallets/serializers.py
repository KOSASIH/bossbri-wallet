# serializers.py

from rest_framework import serializers
from .models import Wallet, WalletTransaction, WalletAddress

class WalletSerializer(serializers.ModelSerializer):
    """
    Serializer for wallets
    """
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'created_at', 'updated_at']

class WalletTransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for wallet transactions
    """
    class Meta:
        model = WalletTransaction
        fields = ['id', 'wallet', 'transaction_type', 'amount', 'description', 'created_at', 'updated_at']

class WalletAddressSerializer(serializers.ModelSerializer):
    """
    Serializer for wallet addresses
    """
    class Meta:
        model = WalletAddress
        fields = ['id', 'wallet', 'address', 'label', 'created_at', 'updated_at']
