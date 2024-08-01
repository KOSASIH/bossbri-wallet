# urls.py

from django.urls import path
from .views import WalletAPIView, WalletTransactionAPIView, WalletAddressAPIView, WalletDetailAPIView

urlpatterns = [
    path('wallets/', WalletAPIView.as_view(), name='wallet_list'),
    path('wallets/<int:pk>/', WalletDetailAPIView.as_view(), name='wallet_detail'),
    path('wallets/transactions/', WalletTransactionAPIView.as_view(), name='wallet_transaction_list'),
    path('wallets/addresses/', WalletAddressAPIView.as_view(), name='wallet_address_list'),
]
