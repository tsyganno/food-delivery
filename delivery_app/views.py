from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django.db.models import Q

from delivery_app.models import Category, Dish, Cart, Order
from delivery_app.forms import CartForm, OrderForm


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
        cart = Cart.objects.filter(user__id=pk_user, active_status=True)
        order_price = 0
        for el in cart:
            count_price = el.dish.price * el.count_of_dishes
            order_price += count_price
        return render(request, 'delivery_app/cart.html', {'cart': cart, 'order_price': order_price})


class CheckoutView(LoginRequiredMixin, CreateView):
    """Оформление заказа"""
    login_url = 'accounts:login'
    template_name = 'delivery_app/checkout.html'
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.order_creation_time = now()
        form.instance.owner = self.request.user
        cart = Cart.objects.filter(user__id=self.request.user.pk, active_status=True)
        list_of_dishes = ''
        count = 1
        order_price = 0
        for el in cart:
            list_of_dishes += f'{count}. Блюдо: {el.dish.title}, цена: {el.dish.price}, количество: {el.count_of_dishes}\n'
            order_price += el.dish.price * el.count_of_dishes
            Cart.objects.filter(pk=el.pk).update(active_status=False)
            count += 1
        list_of_dishes += f'Общая стоимость заказа составляет: {order_price}'
        form.instance.list_of_dishes = list_of_dishes
        return super(CheckoutView, self).form_valid(form)

    def get_success_url(self):
        return reverse('app:success')


class AddToCartFromDishView(LoginRequiredMixin, CreateView):
    """Добавление блюда в корзину для заказа со страницы 'Блюдо'"""
    login_url = 'accounts:login'
    template_name = 'delivery_app/adding_to_cart.html'
    model = Cart
    form_class = CartForm

    def form_valid(self, form):
        form.instance.published_at = now()
        form.instance.user = self.request.user
        form.instance.dish = get_object_or_404(Dish, pk=self.kwargs['dish_id'])
        cart = Cart.objects.filter(user__id=self.request.user.pk, active_status=True, dish__id=self.kwargs['dish_id'])
        total = sum([el.count_of_dishes for el in cart])
        if len(cart) > 0:
            Cart.objects.filter(dish__title=cart.first().dish.title).delete()
            form.instance.count_of_dishes += total
        return super(AddToCartFromDishView, self).form_valid(form)

    def get_success_url(self):
        dish_pk = get_object_or_404(Dish, pk=self.kwargs['dish_id']).pk
        dish_slug = get_object_or_404(Dish, pk=self.kwargs['dish_id']).url_dish
        return reverse('app:dish', args=[dish_pk, dish_slug])


class AddToCartFromCategoryView(LoginRequiredMixin, CreateView):
    """Добавление блюда в корзину для заказа со страницы 'Категория'"""
    login_url = 'accounts:login'
    template_name = 'delivery_app/adding_to_cart.html'
    model = Cart
    form_class = CartForm

    def form_valid(self, form):
        form.instance.published_at = now()
        form.instance.user = self.request.user
        form.instance.dish = get_object_or_404(Dish, pk=self.kwargs['dish_id'])
        cart = Cart.objects.filter(user__id=self.request.user.pk, active_status=True, dish__id=self.kwargs['dish_id'])
        total = sum([el.count_of_dishes for el in cart])
        if len(cart) > 0:
            Cart.objects.filter(dish__title=cart.first().dish.title).delete()
            form.instance.count_of_dishes += total
        return super(AddToCartFromCategoryView, self).form_valid(form)

    def get_success_url(self):
        category_obj_pk = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.pk
        category_obj_slug = get_object_or_404(Dish, pk=self.kwargs['dish_id']).category.url_category
        return reverse('app:category', args=[category_obj_pk, category_obj_slug])


class RemoveFromCartView(LoginRequiredMixin, DeleteView):
    """Удаление блюда из корзины"""
    login_url = 'acc:signin'
    model = Cart

    def get_queryset(self):
        try:
            owner = self.request.user.pk
            variant = int(self.request.POST.getlist('variant')[0])
            return self.model.objects.filter(user__id=owner, id=variant)
        except IndexError:
            return self.model.objects.filter(user__id=-1, id=-1)

    def get_object(self, queryset=None):
        return self.get_queryset()

    def get_success_url(self):
        return reverse('app:cart')


class SuccessView(LoginRequiredMixin, View):
    """Страница с благодарностью за заказ"""
    login_url = 'acc:signin'

    def get(self, request, *args, **kwargs):
        return render(request, 'delivery_app/success.html', context={'title': 'Спасибо'})


class SearchResultsView(LoginRequiredMixin, View):
    """Поиск блюда или категории"""
    login_url = 'acc:signin'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query and query != '':
            print('lol')
            dish_results = Dish.objects.filter(Q(title__icontains=query) | Q(description_dish__icontains=query))
            category_results = Category.objects.filter(Q(name__icontains=query) | Q(description_category__icontains=query))
            all_things = list(dish_results) + list(category_results)
            paginator = Paginator(all_things, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'delivery_app/search.html', context={'title': 'Поиск', 'results': page_obj, 'count': paginator.count})
        return HttpResponseRedirect(reverse('app:index'))
