from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from Service.views import (
    index,
    service_cart,
    service_order,
    service_check_info,
    service_procedure
)

urlpatterns = [
    path('', index),
    path('service_cart',service_cart,name='service_cart'),
    path('service_order',service_order,name='service_order'),
    path('service_check_info',service_check_info,name='service_check_info'),
    path('service_procedure',service_procedure,name='service_procedure')
]