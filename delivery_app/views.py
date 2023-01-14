from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.views import View
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from delivery_app.models import Category, Dish, Cart


class IndexView(View):
    """Стартовая страница с категориями блюд"""
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        paginator = Paginator(categories, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'delivery_app/index.html', {'page_obj': page_obj})


class CategoryView(LoginRequiredMixin, View):
    """Страница с блюдами, относящимся к определенной категории"""
    login_url = 'acc:signin'

    def get(self, request, slug, *args, **kwargs):
        dishes = Dish.objects.filter(category_id=self.kwargs['pk'], category__url_category=self.kwargs['slug'])
        category = get_object_or_404(Category, id=self.kwargs['pk'])
        paginator = Paginator(dishes, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'delivery_app/category_list.html', {'page_obj': page_obj, 'category': category})


class DishView(LoginRequiredMixin, View):
    """Страница с конкретным блюдом"""
    login_url = 'acc:signin'

    def get(self, request, slug, *args, **kwargs):
        dish = get_object_or_404(Dish, id=self.kwargs['pk'])
        return render(request, 'delivery_app/dish.html', {'dish': dish})


class CartView(LoginRequiredMixin, View):
    """Страница с отображением содержимого в корзине"""
    login_url = 'acc:signin'

    def get(self, request, slug, *args, **kwargs):
        pk_user = self.request.user.pk
        cart = get_object_or_404(Cart, user__id=pk_user)
        return render(request, 'delivery_app/cart.html', {'cart': cart})


class AddToCartView(LoginRequiredMixin, View):
    """Добавление блюда в корзину для заказа"""
    login_url = 'acc:signin'

    def get(self, request, *args, **kwargs):
        cart = Cart()
        cart.published_at = timezone.now()
        cart.dish = get_object_or_404(Dish, pk=self.kwargs['dish_id'])
        cart.user = self.request.user
        cart.save()
        category_obj_pk = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.pk
        category_obj_slug = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.url_category
        return HttpResponseRedirect(reverse('app:category', args=[category_obj_pk, category_obj_slug]))
