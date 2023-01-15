from django.shortcuts import render, redirect
from django.shortcuts import reverse
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect
from django.views import View
from django.views.generic import DeleteView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from delivery_app.models import Category, Dish, Cart


def add_to_shopping_cart(request, pk: int):
    cart = Cart()
    cart.published_at = timezone.now()
    cart.dish = get_object_or_404(Dish, pk=pk)
    cart.user = request.user
    cart.save()


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

    def get(self, request, *args, **kwargs):
        pk_user = self.request.user.pk
        cart = Cart.objects.filter(user__id=pk_user)
        order_price = 0
        for el in cart:
            order_price += el.dish.price
        return render(request, 'delivery_app/cart.html', {'cart': cart, 'order_price': order_price})


class AddToCartView(LoginRequiredMixin, View):
    """Добавление блюда в корзину для заказа"""
    login_url = 'acc:signin'

    def post(self, request, slug, *args, **kwargs):
        add_to_shopping_cart(request, self.kwargs['dish_id'])
        category_obj_pk = get_object_or_404(Dish, pk=self.kwargs['dish_id']).pk
        category_obj_slug = get_object_or_404(Dish, pk=self.kwargs['dish_id']).url_dish
        return HttpResponseRedirect(reverse('app:dish', args=[category_obj_pk, category_obj_slug]))

    def get(self, request, slug, *args, **kwargs):
        add_to_shopping_cart(request, self.kwargs['dish_id'])
        category_obj_pk = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.pk
        category_obj_slug = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.url_category
        return HttpResponseRedirect(reverse('app:category', args=[category_obj_pk, category_obj_slug]))


class RemoveFromCartView(LoginRequiredMixin, DeleteView):
    """Удаление блюда из корзины"""
    login_url = 'acc:signin'
    model = Cart

    def get_queryset(self):
        owner = self.request.user.pk
        variant = int(self.request.POST.getlist('variant')[0])
        return self.model.objects.filter(user__id=owner, id=variant)

    def get_object(self, queryset=None):
        return self.get_queryset()

    def get_success_url(self):
        return reverse('app:cart')
