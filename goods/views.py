from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def category(request: HttpRequest) -> HttpResponse:
    return render(request, 'goods/category.html')


def product(request: HttpRequest) -> HttpResponse:
    return render(request, 'goods/product.html')
