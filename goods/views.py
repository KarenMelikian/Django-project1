from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404

from django.views.generic import ListView, DetailView
from .models import Products, Categories



class CategoryListView(ListView):
    model = Products
    template_name = 'goods/category.html'
    context_object_name = 'goods'
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug == 'all':
            queryset = super().get_queryset()
        else:
            queryset = get_list_or_404(super().get_queryset().filter(category__slug=category_slug))
        return queryset

class ProductDetailsView(DetailView):
    template_name = 'goods/product.html'
    model = Products
    context_object_name = 'product'