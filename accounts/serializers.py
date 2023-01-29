from rest_framework import serializers
from accounts import models


class _AccountWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ('id', 'first_name', 'last_name')



class WalletSerializer(serializers.ModelSerializer):
    account = _AccountWalletSerializer(read_only=True)

    class Meta:
        model = models.Wallet
        fields = '__all__'


class _WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Wallet
        fields = (
            'id',
            'amount',
            'amount_currency'
        )


class AccountSerializer(serializers.ModelSerializer):
    # wallets = _WalletSerializer(read_only=True, many=True)
    # wallets = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
     
    class Meta:
        model = models.Account
        fields = ('__all__')
