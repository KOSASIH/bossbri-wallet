from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/bri_api/', include('bri_api.urls')),
    path('api/v1/transactions/', include('transactions.urls')),
    path('api/v1/wallets/', include('wallets.urls')),
]
