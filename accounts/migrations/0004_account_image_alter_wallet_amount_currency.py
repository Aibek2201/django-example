# Generated by Django 4.1.5 on 2023-02-04 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_wallet_amount_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='amount_currency',
            field=models.CharField(choices=[('RUB', 'Рубль'), ('KZT', 'Теңге'), ('USD', 'Доллар')], default='KZT', max_length=3),
        ),
    ]
