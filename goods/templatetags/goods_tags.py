from django import template

from goods.models import Categories, Products

register = template.Library()


@register.simple_tag()
def category_tag():
    return Categories.objects.all()


@register.simple_tag()
def product_tag():
    return Products.objects.all()