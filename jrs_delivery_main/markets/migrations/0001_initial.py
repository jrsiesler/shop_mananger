# Generated by Django 4.2 on 2023-05-08 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Markets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='razao social:')),
                ('common_name', models.CharField(max_length=60, verbose_name='nome fantasia:')),
                ('document_number', models.BigIntegerField(max_length=14, verbose_name='cnpj:')),
                ('creation_date', models.DateTimeField(null=True, verbose_name='data criacao')),
            ],
        ),
        migrations.CreateModel(
            name='MarketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MarketIntegrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_channel', models.CharField(choices=[('WTZ', 'WHATSAPP'), ('ITG', 'INSTAGRAN'), ('FBK', 'FACEBOOK'), ('GOG', 'GOOGLE'), ('IFD', 'IFOOD')], default='MKT', max_length=3, verbose_name='canal de vendas: ')),
                ('integration_host', models.CharField(max_length=255, null=True)),
                ('integration_id', models.BooleanField(null=True, verbose_name='integra com ifood')),
                ('id_ifood', models.UUIDField(null=True, verbose_name='id da loja ifood')),
                ('access_key', models.CharField(max_length=50, null=True, verbose_name='access-key ou client-id: ')),
                ('secret_access_key', models.CharField(max_length=50, null=True, verbose_name='secret-key ou client-secret: ')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.markets')),
            ],
        ),
        migrations.CreateModel(
            name='MarketAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adrress', models.CharField(max_length=100, verbose_name='endreço:')),
                ('address_number', models.IntegerField(max_length=10, verbose_name='numero:')),
                ('address_details', models.CharField(max_length=50, verbose_name='complemento:')),
                ('address_neighborhood', models.CharField(max_length=50, verbose_name='bairro:')),
                ('address_city', models.CharField(max_length=60, verbose_name='municipio')),
                ('address_state', models.CharField(max_length=2, verbose_name='estado:')),
                ('address_country', models.CharField(max_length=50, verbose_name='pais:')),
                ('address_postal_code', models.IntegerField(max_length=8, verbose_name='codigo postal:')),
                ('creation_date', models.DateTimeField(verbose_name='data de cadastro:')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='markets.markets')),
            ],
        ),
    ]
