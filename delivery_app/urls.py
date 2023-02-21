from django.urls import path

from delivery_app.views import IndexView, CategoryView, DishView, CartView, AddToCartFromDishView, \
    AddToCartFromCategoryView, RemoveFromCartView, CheckoutView, SuccessView, SearchResultsView, AllDishesView, \
    MyOrdersView, CartUpdateView, FeedBackView, ContactSuccessView

app_name = 'app'
urlpatterns = [
    path('categories/', IndexView.as_view(), name='index'),
    path('all_dishes/', AllDishesView.as_view(), name='all_dishes'),
    path('my_orders/', MyOrdersView.as_view(), name='my_orders'),
    path('category/<int:pk>/<slug>/', CategoryView.as_view(), name='category'),
    path('dishes/<int:pk>/<slug>/', DishView.as_view(), name='dish'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/change_quantity/<int:cart_id>/', CartUpdateView.as_view(), name='change_quantity'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('remove_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('add_to_cart_from_category/<int:dish_id>/<slug>/', AddToCartFromDishView.as_view(), name='add_to_cart_from_dish'),
    path('add_to_cart_from_dish/<int:dish_id>/<slug>/', AddToCartFromCategoryView.as_view(), name='add_to_cart_from_category'),
    path('success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
]
