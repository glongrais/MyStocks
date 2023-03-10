# Generated by Django 4.1.7 on 2023-02-17 13:09

from django.db import migrations

def create_data(apps, schema_editor):
    Stock = apps.get_model('stocks', 'Stock')
    Stock(symbol= "AI.PA", name="Air Liquide", currentPrice=1.0, previousClose=1.0, sector="industry", dividendYield=0.0, logoUrl="www.google.com").save()



class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]