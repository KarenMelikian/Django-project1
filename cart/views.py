from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView

class CartAddView(CreateView):
    template_name = 'cart/cart-add.html'


class CartChangeView(UpdateView):
    template_name = 'cart/cart-change.html'


class CartRemoveView(DeleteView):
    template_name = 'cart/cart-remove.html'
