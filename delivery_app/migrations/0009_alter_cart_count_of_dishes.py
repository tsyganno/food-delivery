# Generated by Django 4.1.4 on 2023-01-22 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0008_alter_cart_count_of_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count_of_dishes',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Количество блюд'),
        ),
    ]
