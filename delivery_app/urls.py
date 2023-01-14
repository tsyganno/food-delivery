from django.urls import path

from delivery_app.views import IndexView, CategoryView, DishView, CartView, AddToCartView

app_name = 'app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/<slug>/', CategoryView.as_view(), name='category'),
    path('dishes/<int:pk>/<slug>/', DishView.as_view(), name='dish'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<int:dish_id>/', AddToCartView.as_view(), name='add_to_cart'),
]
