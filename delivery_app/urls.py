from django.urls import path

from delivery_app.views import IndexView, CategoryDetailView

app_name = 'app'
urlpatterns = [
    path('categories/', IndexView.as_view(), name='index'),
    path('categories/<int:pk>/<slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
