# urls.py

from django.urls import path
from .views import TransactionAPIView, WalletAPIView, TransactionDetailAPIView

urlpatterns = [
    path('transactions/', TransactionAPIView.as_view(), name='transaction_list'),
    path('transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction_detail'),
    path('wallets/', WalletAPIView.as_view(), name='wallet_list'),
    path('wallets/<int:pk>/', WalletAPIView.as_view(), name='wallet_detail'),
]
