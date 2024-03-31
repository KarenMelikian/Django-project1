from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
from .models import ProductsKitchen


class CategoryKitchenView(ListView):
    template_name = 'goods/category.html'
    model = ProductsKitchen
    context_object_name = 'kitchen'


def product(request: HttpRequest) -> HttpResponse:
    return render(request, 'goods/product.html')