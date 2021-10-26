from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from aboutus.views import (
    index,

)

urlpatterns = [
    path('', index),

]