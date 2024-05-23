from django.urls import path
from .views import create_order, OrderListView

app_name = 'order'


urlpatterns = [
    path('create-order/', create_order, name='create_order'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
]