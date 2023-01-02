from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Стартовая страница"""
    def get(self, request, *args, **kwargs):
        return render(request, 'delivery_app/index.html')
