from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DeleteView, UpdateView

from goods.models import Products

from .models import Cart


class CartAddView(View):
    def get(self, request, product_slug):
        product = Products.objects.get(slug=product_slug)

        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)

            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)

        return redirect(request.META['HTTP_REFERER'])


class CartChangeView(UpdateView):
    template_name = 'cart/cart-change.html'


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
