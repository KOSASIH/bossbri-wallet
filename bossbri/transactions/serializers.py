# serializers.py

from rest_framework import serializers
from .models import Transaction, Wallet

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for transactions
    """
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'transaction_type', 'amount', 'description', 'created_at', 'updated_at']

class WalletSerializer(serializers.ModelSerializer):
    """
    Serializer for wallets
    """
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance', 'created_at', 'updated_at']
