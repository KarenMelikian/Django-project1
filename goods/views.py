from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from .models import Products_kitchen


class CategoryKitchenView(ListView):
    template_name = 'goods/category.html'
    model = Products_kitchen
    context_object_name = 'kitchen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['kitchen']:
            product.discounted_price = round(product.price - (product.price * product.discount / 100), 2)
        return context


def product(request: HttpRequest) -> HttpResponse:
    return render(request, 'goods/product.html')
