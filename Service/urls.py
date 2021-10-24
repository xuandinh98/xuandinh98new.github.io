from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from Service.views import (
    index,
    service_cart,
    service_order
)

urlpatterns = [
    path('', index),
    path('service_cart',service_cart,name='service_cart'),
    path('service_order',service_order,name='service_order')
]