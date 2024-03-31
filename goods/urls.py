from django.urls import path

from .views import (ProductListView,
                    ProductDetailsView)
app_name = 'goods'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product')
]