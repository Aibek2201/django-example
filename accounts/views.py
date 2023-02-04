from rest_framework.viewsets import ModelViewSet

from accounts import serializers, models, filters, services


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account')
    serializer_class = serializers.WalletSerializer
    filterset_class = filters.WalletFilter


class AccountViewSet(ModelViewSet):
    account_services = services.AccountServicesV1()
    queryset = account_services.get_account()
    serializer_class = serializers.AccountSerializer

    def perform_create(self, serializer: serializers.AccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)


