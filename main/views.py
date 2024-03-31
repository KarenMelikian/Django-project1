from django.http import HttpRequest, HttpResponse
from django.shortcuts import render



def index(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'RegalRidge - Main',
        'content': 'RegalRidge Furniture Store',
    }

    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'RegalRidge - About Us',
        'content': 'About Us',
        'text_on_page': '''
        Welcome to RegalRidge! Discover stylish furniture for every room in your home.
        From cozy sofas to elegant dining sets,
        we have what you need to create your dream space.
        Shop now and elevate your home with RegalRidge's exquisite collection.'''
    }

    return render(request, 'main/about.html', context)