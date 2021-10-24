from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response
# Create your views here.
def index(request):
    return render(request, 'pages_service/service_template.html')
def service_cart(request):
    return render(request, 'pages_service/service_cart.html')
def service_order(request):
    return render(request, 'pages_service/service_order.html')
