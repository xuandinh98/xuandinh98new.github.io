from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response
# Create your views here.
def index(request):
    return render(request, 'pages_aboutus/aboutus_template.html')
