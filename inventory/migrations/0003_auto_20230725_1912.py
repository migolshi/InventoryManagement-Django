# Generated by Django 3.0.7 on 2023-07-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_stock_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
