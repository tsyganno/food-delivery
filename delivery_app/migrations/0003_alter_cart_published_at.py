# Generated by Django 4.1.4 on 2023-01-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0002_cart_count_of_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='published_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Заказ создан'),
        ),
    ]
