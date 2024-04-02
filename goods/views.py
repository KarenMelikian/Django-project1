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
        on_sale = self.request.GET.get('on_sale', None)
        order_by = self.request.GET.get('order_by', None)

        queryset = super().get_queryset()

        if category_slug != 'all':
            queryset = queryset.filter(category__slug=category_slug)

        if on_sale:
            queryset = queryset.filter(discount__gt=0)

        if order_by and order_by != 'default':
            queryset = queryset.order_by(order_by)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_slug'] = self.kwargs.get('category_slug', None)
        return context


class ProductDetailsView(DetailView):
    template_name = 'goods/product.html'
    model = Products
    context_object_name = 'product'