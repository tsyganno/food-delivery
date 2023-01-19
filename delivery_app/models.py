from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    url_category = models.SlugField()
    description_category = RichTextUploadingField(verbose_name='Описание категории')
    image_category = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


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
    published_at = models.DateTimeField(default=now(), verbose_name='Заказ создан')
    active_status = models.BooleanField(default=True, verbose_name='Статус')
    count_of_dishes = models.IntegerField(default=1, verbose_name='Количество блюд')
    dish = models.ForeignKey(Dish, null=True, on_delete=models.CASCADE, verbose_name='Блюдо')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return 'Заказ клиента'

    class Meta:
        verbose_name_plural = 'Заказы клиентов'
        verbose_name = 'Заказ клиента'
        ordering = ['published_at']
