from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    RUB = 'RUB', 'Рубль'
    KZT = 'KZT', 'Теңге'
    USD = 'USD', 'Доллар'