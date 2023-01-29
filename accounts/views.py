from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from accounts import serializers, models, filters


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account')
    serializer_class = serializers.WalletSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter


class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.prefetch_related(
        'wallets',
    )
    serializer_class = serializers.AccountSerializer

