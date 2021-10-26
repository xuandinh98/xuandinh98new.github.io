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
    statistics_revenue,
    phieu_rut_tien,
    phieu_thay_doi_thong_tin,
    phieu_huy_doi_tac,
    order_receive,
    chat,
    registerWithdrawal
    
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
    path('phieu_rut_tien', phieu_rut_tien, name = 'phieu_rut_tien'),
    path('phieu_thay_doi_thong_tin', phieu_thay_doi_thong_tin, name = 'phieu_thay_doi_thong_tin'),
    path('phieu_huy_doi_tac', phieu_huy_doi_tac, name = 'phieu_huy_doi_tac'),
    path('order_receive', order_receive, name = 'order_receive'),
    path('chat', chat, name = 'chat'),
    path('registerWithdrawal', registerWithdrawal, name = 'registerWithdrawal'),
    
]