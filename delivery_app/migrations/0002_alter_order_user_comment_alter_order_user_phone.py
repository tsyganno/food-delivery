# Generated by Django 4.1.4 on 2023-01-29 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_comment',
            field=models.TextField(default='', verbose_name='Комментарий от пользователя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_phone',
            field=models.CharField(default='', max_length=50, verbose_name='Номер телефона'),
        ),
    ]