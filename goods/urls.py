from django.urls import path

from .views import (CategoryKitchenView,
                    product)
app_name = 'goods'

urlpatterns = [
    path('', CategoryKitchenView.as_view(), name='index'),
    path('product/', product, name='product')
]