# Generated by Django 4.1.4 on 2023-01-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0002_dish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
    ]
