from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from Partner.views import (
    index,
    postProvinces, 
    addPartner,
)

urlpatterns = [
    path('', index),
    path('post/postProvinces', postProvinces, name = 'postProvinces'),
    path('post/addPartner', addPartner, name = 'addPartner'),
]