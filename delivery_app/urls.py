from django.urls import path

from delivery_app.views import IndexView, CategoryView, DishView, CartView, AddToCartFromDishView, \
    AddToCartFromCategoryView, RemoveFromCartView, CheckoutView

app_name = 'app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/<slug>/', CategoryView.as_view(), name='category'),
    path('dishes/<int:pk>/<slug>/', DishView.as_view(), name='dish'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('remove_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('add_to_cart_from_category/<int:dish_id>/<slug>/', AddToCartFromDishView.as_view(), name='add_to_cart_from_dish'),
    path('add_to_cart_from_dish/<int:dish_id>/<slug>/', AddToCartFromCategoryView.as_view(), name='add_to_cart_from_category'),
]
