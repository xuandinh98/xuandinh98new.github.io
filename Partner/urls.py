from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from Partner.views import (
    index,
    postProvinces, 
)

urlpatterns = [
    path('', index),
    path('post/ajax/postProvinces', postProvinces, name = 'postProvinces'),
]