from django.urls import path

from .views import (CategoryListView,
                    ProductDetailsView)
app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', CategoryListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product')
]