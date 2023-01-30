# Generated by Django 4.1.4 on 2023-01-30 14:53

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('url_category', models.SlugField()),
                ('description_category', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание категории')),
                ('image_category', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_creation_time', models.DateTimeField(verbose_name='Заказ создан')),
                ('list_of_dishes', models.TextField(verbose_name='Блюда в заказе')),
                ('order_status', models.BooleanField(default=True, verbose_name='Статус заказа')),
                ('payment_method', models.CharField(choices=[('Оплата картой', 'Оплата картой'), ('Оплата наличными', 'Оплата наличными'), ('Оплата переводом через банк', 'Оплата переводом через банк')], max_length=50, verbose_name='Способ оплаты')),
                ('user_phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес (не больше 100 символов)')),
                ('user_comment', models.TextField(default='', verbose_name='Комментарий от пользователя')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ клиента',
                'verbose_name_plural': 'Заказы клиентов',
                'ordering': ['order_creation_time'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('url_dish', models.SlugField()),
                ('description_dish', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание блюда')),
                ('image_dish', models.ImageField(upload_to='')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='delivery_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_at', models.DateTimeField(verbose_name='Блюдо добавлено в корзину')),
                ('active_status', models.BooleanField(default=True, verbose_name='Статус блюда в корзине')),
                ('count_of_dishes', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)], verbose_name='Количество блюд')),
                ('dish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery_app.dish', verbose_name='Блюдо')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Блюдо в корзине',
                'verbose_name_plural': 'Блюда в корзине',
                'ordering': ['published_at'],
            },
        ),
    ]
