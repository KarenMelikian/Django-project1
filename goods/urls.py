from django.urls import path

from .views import (category,
                    product)
app_name = 'goods'

urlpatterns = [
    path('', category, name='index'),
    path('product/', product, name='about')
]