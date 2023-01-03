from django.shortcuts import render
from django.views import View

from delivery_app.models import Category


class IndexView(View):
    """Стартовая страница"""
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'delivery_app/index.html', {'categories': categories})
