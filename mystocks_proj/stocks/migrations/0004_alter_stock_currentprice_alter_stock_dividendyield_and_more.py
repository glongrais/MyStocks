# Generated by Django 4.1.7 on 2023-02-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0003_stockholding"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="currentPrice",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="stock",
            name="dividendYield",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="stock",
            name="previousClose",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
