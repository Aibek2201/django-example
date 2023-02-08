from rest_framework.viewsets import ModelViewSet

from accounts import serializers, models, filters, services


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account')
    serializer_class = serializers.WalletSerializer
    filterset_class = filters.WalletFilter
    pagination_class = None


class AccountViewSet(ModelViewSet):
    account_services = services.AccountServicesV1()
    filterset_class = filters.AccountFilter

    def get_serializer_class(self):
        account_serializers = {
            'create': serializers.CreateAccountSerializer,
            'list': serializers.ListAccountSerializer,
        }

        return account_serializers.get(self.action, serializers.RetrieveAccountSerializer)

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    def perform_create(self, serializer: serializers.CreateAccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)


class AccountViewSetV2(ModelViewSet):
    account_services = services.AccountServicesV1()
    serializer_class = serializers.RetrieveAccountSerializer
    filterset_class = filters.AccountFilter

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

