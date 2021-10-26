from django.shortcuts import render
from .models import Provinces
from .models import Districts
from .models import Wards
from .models import Partner
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import date
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.http import HttpResponse, response
# Create your views here.


@csrf_protect
def index(request):
    Data = {'Provinces' : Provinces.objects.all().order_by('name')}
    return render(request, 'pages/partner_template.html', Data)

def partner_admin(request):
    return render(request, 'pages/admin/dashboard.html')

def partner_ticket(request):
    return render(request, 'pages/admin/partner_ticket.html')

def partner_order(request):
    return render(request, 'pages/admin/partner_order.html')

def partner_info(request):
    return render(request, 'pages/admin/partner_info.html')

def statistics_revenue(request):
    return render(request, 'pages/admin/statistics_revenue.html')

def phieu_rut_tien(request):
    return render(request, 'pages/admin/phieu_rut_tien.html')

def phieu_thay_doi_thong_tin(request):
    return render(request, 'pages/admin/phieu_thay_doi_thong_tin.html')

def phieu_huy_doi_tac(request):
    return render(request, 'pages/admin/phieu_huy_doi_tac.html')
    
def order_receive(request):
    return render(request, 'pages/admin/order_receive.html')

def chat(request):
    return render(request, 'pages/admin/chat.html')

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
        if requestType == "4":
            Data = Wards.objects.filter(district_id=parameter)
            qs_json = serializers.serialize('json', Data)
            return JsonResponse(qs_json, content_type='application/json', safe=False)
    # some error occured
    return JsonResponse({"error": "ahihi"}, status=400)

def addPartner(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        today = date.today()
        partner = Partner()

        # add image avatar
        avatar = request.FILES.get('avatar')
        fss = FileSystemStorage()
        filename = fss.save(avatar.name, avatar)
        partner.partner_image = filename
        
        # add image store_image
        store_image = request.FILES.get('image_store')
        fss = FileSystemStorage()
        filename = fss.save(store_image.name, store_image)
        partner.store_image = filename

        # add image partner_CMND_image_front
        partner_CMND_image_front = request.FILES.get('cmnd_pic_front')
        fss = FileSystemStorage()
        filename = fss.save(partner_CMND_image_front.name, partner_CMND_image_front)
        partner.partner_CMND_image_front = filename

        # add image partner_CMND_image_back
        partner_CMND_image_back = request.FILES.get('cmnd_pic_back')
        fss = FileSystemStorage()
        filename = fss.save(partner_CMND_image_back.name, partner_CMND_image_back)
        partner.partner_CMND_image_back = filename

        # add image police_certificate
        police_certificate = request.FILES.get('certification')
        fss = FileSystemStorage()
        filename = fss.save(police_certificate.name, police_certificate)
        partner.police_certificate = filename

        partner.username = request.POST['username']
        partner.password = request.POST['password']
        partner.partner_firstname = request.POST['firstname']
        partner.partner_lastname = request.POST['lastname']
        partner.partner_sex = request.POST['sex']
        partner.store_name = request.POST['store_name']
        partner.partner_phone = request.POST['phone1']
        partner.partner_phone2 = request.POST['phone2']
        partner.partner_CMND = request.POST['cmnd']
        partner.partner_CMND_date_created = request.POST['cmnd_date_issue']
        partner.partner_CMND_address = request.POST['cmnd_address']
        partner.partner_CMND_issued = request.POST['cmnd_place_issue']
        partner.partner_birthday = request.POST['cmnd_birthday']
        partner.partner_email = request.POST['email']
        partner.partner_address = request.POST['store_address']
        partner.partner_area = request.POST['store_nation']
        partner.partner_province = request.POST['store_province']
        partner.partner_district = request.POST['store_district']
        partner.partner_wards = request.POST['store_wards']
        partner.partner_recruitment_source = request.POST['recruitment-source']
        partner.partner_bank_account = request.POST['bank_number']
        partner.bank_name = request.POST['bank']
        partner.bank_account_holder_name = request.POST['bank_name']
        partner.bank_branch = request.POST['bank_branch']
        partner.partner_slug = "check-slug"
        partner.partner_status = "1"
        partner.partner_desc = ""
        partner.partner_coin = "0"
        partner.partner_total_order = "0"
        partner.partner_total_revenue = "0"
        partner.partner_total_profit = "0"
        partner.created_at = today
        partner.updated_at = today
        partner.typerepair_xedap = request.POST['xedap']
        partner.typerepair_xemay = request.POST['xemay']
        partner.typerepair_xehoi = request.POST['xehoi']
        partner.typerepair_xekeo = request.POST['xekeo']
        
        
        partner.save()

        return JsonResponse({"error": "false"})

def registerWithdrawal(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        today = date.today()
        partner = Partner()

        # add image avatar
        avatar = request.FILES.get('avatar')
        fss = FileSystemStorage()
        filename = fss.save(avatar.name, avatar)
        partner.partner_image = filename
        
        # add image store_image
        store_image = request.FILES.get('image_store')
        fss = FileSystemStorage()
        filename = fss.save(store_image.name, store_image)
        partner.store_image = filename

        # add image partner_CMND_image_front
        partner_CMND_image_front = request.FILES.get('cmnd_pic_front')
        fss = FileSystemStorage()
        filename = fss.save(partner_CMND_image_front.name, partner_CMND_image_front)
        partner.partner_CMND_image_front = filename

        # add image partner_CMND_image_back
        partner_CMND_image_back = request.FILES.get('cmnd_pic_back')
        fss = FileSystemStorage()
        filename = fss.save(partner_CMND_image_back.name, partner_CMND_image_back)
        partner.partner_CMND_image_back = filename

        # add image police_certificate
        police_certificate = request.FILES.get('certification')
        fss = FileSystemStorage()
        filename = fss.save(police_certificate.name, police_certificate)
        partner.police_certificate = filename

        partner.username = request.POST['username']
        partner.password = request.POST['password']
        partner.partner_firstname = request.POST['firstname']
        partner.partner_lastname = request.POST['lastname']
        partner.partner_sex = request.POST['sex']
        partner.store_name = request.POST['store_name']
        partner.partner_phone = request.POST['phone1']
        partner.partner_phone2 = request.POST['phone2']
        partner.partner_CMND = request.POST['cmnd']
        partner.partner_CMND_date_created = request.POST['cmnd_date_issue']
        partner.partner_CMND_address = request.POST['cmnd_address']
        partner.partner_CMND_issued = request.POST['cmnd_place_issue']
        partner.partner_birthday = request.POST['cmnd_birthday']
        partner.partner_email = request.POST['email']
        partner.partner_address = request.POST['store_address']
        partner.partner_area = request.POST['store_nation']
        partner.partner_province = request.POST['store_province']
        partner.partner_district = request.POST['store_district']
        partner.partner_wards = request.POST['store_wards']
        partner.partner_recruitment_source = request.POST['recruitment-source']
        partner.partner_bank_account = request.POST['bank_number']
        partner.bank_name = request.POST['bank']
        partner.bank_account_holder_name = request.POST['bank_name']
        partner.bank_branch = request.POST['bank_branch']
        partner.partner_slug = "check-slug"
        partner.partner_status = "1"
        partner.partner_desc = ""
        partner.partner_coin = "0"
        partner.partner_total_order = "0"
        partner.partner_total_revenue = "0"
        partner.partner_total_profit = "0"
        partner.created_at = today
        partner.updated_at = today
        partner.typerepair_xedap = request.POST['xedap']
        partner.typerepair_xemay = request.POST['xemay']
        partner.typerepair_xehoi = request.POST['xehoi']
        partner.typerepair_xekeo = request.POST['xekeo']
        
        
        partner.save()

        return JsonResponse({"error": "false"})
            
    # some error occured
    return JsonResponse({"error": "ahihi"}, status=400)


