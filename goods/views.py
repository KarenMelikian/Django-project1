from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Products


class ProductListView(ListView):
    template_name = 'goods/category.html'
    model = Products
    context_object_name = 'goods'


class ProductDetailsView(DetailView):
    template_name = 'goods/product.html'
    model = Products
    context_object_name = 'product'