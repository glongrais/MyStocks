# Generated by Django 4.1.7 on 2023-02-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20, verbose_name='Symbol')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('currentPrice', models.FloatField(verbose_name='CurrentPrice')),
                ('previousClose', models.FloatField(verbose_name='PreviousClose')),
                ('sector', models.CharField(max_length=50, verbose_name='Sector')),
                ('dividendYield', models.FloatField(verbose_name='DividendYield')),
                ('logoUrl', models.CharField(max_length=240, verbose_name='LogoURL')),
            ],
        ),
    ]
