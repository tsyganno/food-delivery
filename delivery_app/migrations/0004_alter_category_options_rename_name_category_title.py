# Generated by Django 4.1.4 on 2023-02-01 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_app', '0003_alter_order_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]