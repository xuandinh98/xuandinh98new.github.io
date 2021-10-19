from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from Partner.views import (
    index,
    postProvinces, 
    addPartner,
    partner_admin,
    partner_ticket,
    partner_order,
    partner_info,
    statistics_revenue
)

urlpatterns = [
    path('', index),
    path('post/postProvinces', postProvinces, name = 'postProvinces'),
    path('post/addPartner', addPartner, name = 'addPartner'),
    path('partner_admin', partner_admin, name = 'partner_admin'),
    path('partner_ticket', partner_ticket, name = 'partner_ticket'),
    path('partner_order', partner_order, name = 'partner_order'),
    path('partner_info', partner_info, name = 'partner_info'),
    path('statistics_revenue', statistics_revenue, name = 'statistics_revenue'),
]