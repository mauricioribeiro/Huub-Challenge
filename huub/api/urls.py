from django.urls import path

from .views import order_view, order_products_view

urlpatterns = [
    path('orders', order_view, name='api-orders'),
    path('orders/products', order_products_view, name='api-orders-products'),
]