from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блюда'
        verbose_name = 'Блюдо'
        ordering = ['title']


class Order(models.Model):
    published_at = models.DateTimeField(verbose_name='Заказ создан')
    dish = models.ManyToManyField(Dish, related_name="dish_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return 'Заказ клиента'

    class Meta:
        verbose_name_plural = 'Заказы клиентов'
        verbose_name = 'Заказ клиента'
        ordering = ['published_at']
