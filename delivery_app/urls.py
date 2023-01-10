from django.urls import path

from delivery_app.views import IndexView, CategoryView, DishView

app_name = 'app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/<slug>/', CategoryView.as_view(), name='category'),
    path('dishes/<int:pk>/<slug>/', DishView.as_view(), name='dish'),
]
