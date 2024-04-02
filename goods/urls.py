from django.urls import path

from .views import (CategoryListView,
                    ProductDetailsView)
app_name = 'goods'

urlpatterns = [
    path('search/', CategoryListView.as_view(), name='search'),
    path('<slug:category_slug>/', CategoryListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailsView.as_view(), name='product')
]