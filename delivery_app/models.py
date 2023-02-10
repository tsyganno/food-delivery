from collections import OrderedDict
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    url_category = models.SlugField()
    description_category = RichTextUploadingField(verbose_name='Описание категории')
    image_category = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['title']


class Dish(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название блюда')
    url_dish = models.SlugField()
    description_dish = RichTextUploadingField(verbose_name='Описание блюда')
    image_dish = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="category", verbose_name='Категория')
    price = models.IntegerField(null=True, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = 'Блюдо'
        ordering = ['title']


class Cart(models.Model):
    published_at = models.DateTimeField(verbose_name='Блюдо добавлено в корзину')
    active_status = models.BooleanField(default=True, verbose_name='Статус блюда в корзине')
    count_of_dishes = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(1000), MinValueValidator(1)], verbose_name='Количество блюд')
    dish = models.ForeignKey(Dish, null=True, on_delete=models.CASCADE, verbose_name='Блюдо')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return 'Блюдо в корзине'

    class Meta:
        verbose_name_plural = 'Блюда в корзине'
        verbose_name = 'Блюдо в корзине'
        ordering = ['published_at']


class Order(models.Model):

    ACCEPTED = 'Принят'
    IN_PROGRESS = 'В процессе'
    COMPLETED = 'Выполнен'
    CANCELED = 'Отменен'

    PAYMENT_BY_CARD = 'Оплата картой'
    CASH_PAYMENT = 'Оплата наличными'
    BANK_TRANSFER = 'Оплата переводом через банк'

    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    order_creation_time = models.DateTimeField(verbose_name='Заказ создан')
    list_of_dishes = models.TextField(verbose_name='Блюда в заказе')
    TYPE_DICT_STATUS_ORDER = OrderedDict((
        (ACCEPTED, 'Принят'),
        (IN_PROGRESS, 'В процессе'),
        (COMPLETED, 'Выполнен'),
        (CANCELED, 'Отменен'),
    ))
    order_status = models.CharField(max_length=50, default=ACCEPTED, choices=TYPE_DICT_STATUS_ORDER.items(), verbose_name='Статус заказа')
    TYPE_DICT_PAYMENT = OrderedDict((
        (PAYMENT_BY_CARD, 'Оплата картой'),
        (CASH_PAYMENT, 'Оплата наличными'),
        (BANK_TRANSFER, 'Оплата переводом через банк'),
    ))
    payment_method = models.CharField(max_length=50, choices=TYPE_DICT_PAYMENT.items(), verbose_name='Способ оплаты')
    user_phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, verbose_name='Адрес (не больше 100 символов)')
    user_comment = models.TextField(default='', verbose_name='Комментарий от пользователя')

    def __str__(self):
        return 'Заказ клиента'

    class Meta:
        verbose_name_plural = 'Заказы клиентов (Работает администратор!!!)'
        verbose_name = 'Заказ клиента'
        ordering = ['order_creation_time']


class Logo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название логотипа')
    image_category = models.ImageField()

    def __str__(self):
        return 'Логотип'

    class Meta:
        verbose_name_plural = 'Логотипы'
        verbose_name = 'Логотип'
        ordering = ['name']
