from django.shortcuts import render
from .models import Provinces
from .models import Districts
from .models import Wards
from .forms import ProvincesForm
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.core import serializers
import json

# Create your views here.
from django.http import HttpResponse, response
# Create your views here.


@csrf_protect
def index(request):
    Data = {'Provinces' : Provinces.objects.all().order_by('name')}
    return render(request, 'pages/partner_template.html', Data)

def postProvinces(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        requestType = request.POST['type']
        parameter = request.POST['data']
        if requestType == "1":
            Data = Provinces.objects.all()
            qs_json = serializers.serialize('json', Data)
            return JsonResponse(qs_json, content_type='application/json', safe=False)
        if requestType == "2":
            Data = Districts.objects.filter(province_id=parameter)
            qs_json = serializers.serialize('json', Data)
            return JsonResponse(qs_json, content_type='application/json', safe=False)
        if requestType == "3":
            Data = Wards.objects.filter(district_id=parameter)
            qs_json = serializers.serialize('json', Data)
            return JsonResponse(qs_json, content_type='application/json', safe=False)

        
        # # get the form data
        # form = ProvincesForm(request.POST)
        # # save the data and after fetch the object in instance
        # if form.is_valid():
        #     instance = form.save()
        #     # serialize in new friend object in json
        #     ser_instance = serializers.serialize('json', [ instance, ])
        #     # send to client side.
        #     return JsonResponse({"instance": ser_instance}, status=200)
        # else:
        #     # some form errors occured.
        #     return JsonResponse({"error": form.errors}, status=400)
    

    # some error occured
    return JsonResponse({"error": "ahihi"}, status=400)


