from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

import hashlib

def save(self, *args, **kwargs):        
    self.password = hashlib.md5.new(self.field).digest()
    super().save(*args, **kwargs)

# Create your models here.
class Partner(models.Model):
    STT = models.BigAutoField(primary_key = True)
    partner_id = models.CharField(max_length=10) 
    username = models.TextField() # tên đăng nhập
    password = models.CharField(max_length=16) # mật khẩu
    partner_firstname = models.TextField() # Họ và chữ lót
    partner_lastname = models.TextField(null=True) # Tên đối tác
    partner_sex = models.IntegerField(null=True) # Giới tính 1=>Nam / 2=>Nữ
    partner_image = models.ImageField(upload_to='static/fileupload/', null=True, blank=True) # ảnh hồ sơ
    store_name = models.TextField() # tên cửa hàng
    store_image = models.ImageField(upload_to='static/fileupload/', blank=True) # ảnh cửa hàng
    partner_phone = models.CharField(max_length=11)
    partner_phone2 = models.CharField(max_length=11)
    partner_CMND = models.CharField(max_length=20)
    partner_CMND_date_created = models.DateField() # ngày cấp CMND
    partner_CMND_address = models.TextField() # địa chỉ trên CMND
    partner_CMND_issued = models.TextField() # nơi cấp CMND
    partner_birthday = models.DateField()
    partner_CMND_image_front = models.ImageField(upload_to='static/fileupload/', blank=True) # ảnh mặt trước CMND
    partner_CMND_image_back = models.ImageField(upload_to='static/fileupload/', blank=True) # ảnh mặt sau CMND
    partner_email = models.TextField()
    partner_address = models.TextField()
    partner_area = models.TextField() # quốc gia
    partner_province = models.TextField() # tỉnh/thành
    partner_district = models.TextField() # quận/huyện
    partner_wards = models.TextField() # phường/xã/thị trấn
    partner_recruitment_source = models.TextField() # nguồn tuyển dụng
    police_certificate = models.FileField(upload_to='static/fileupload/', blank=True) # giấy xác nhận của công an như sơ yếu lý lịch,... nếu nhiều để chung 1 file
    partner_bank_account = models.TextField() # tài khoản ngân hàng
    bank_name = models.TextField() # tên ngân hàng
    bank_account_holder_name = models.CharField(max_length=255) # tên tài khoản ngân hàng, viết hoa không dấu
    bank_branch = models.TextField(null=True) # chi nhánh ngân hàng
    partner_slug = models.CharField(max_length=255)
    partner_status = models.IntegerField() # 1=>đăng kí / 2=>làm việc / 0=>ngưng làm
    partner_desc = models.TextField() # nếu đăng kí không thành công => ghi lý do / nếu đăng ký thành công => ghi chú
    partner_coin = models.IntegerField() # số xu trong tài khoản
    partner_total_order = models.IntegerField() # tổng đơn hàng đã nhận
    partner_total_revenue = models.IntegerField() # tổng doanh thu
    partner_total_profit = models.IntegerField() # tổng lợi nhuận từ đối tác
    typerepair_xedap = models.IntegerField(null=True) # sửa xe đạp. 1=> có, 0=> không
    typerepair_xemay = models.IntegerField(null=True) # sửa xe máy. 1=> có, 0=> không
    typerepair_xehoi = models.IntegerField(null=True) # sửa xe hơi. 1=> có, 0=> không
    typerepair_xekeo = models.IntegerField(null=True) # xe kéo. 1=> có, 0=> không
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __int__(self):
        return self.STT
    
    def admin_photo(self):
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % (self.partner_image.url))
    admin_photo.short_description = 'Image'
    admin_photo.alow_tags = True


class Provinces(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.TextField(blank=True)
    gso_id = models.TextField(blank=True)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(blank=True)

class Districts(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.TextField()
    gso_id = models.TextField()
    province_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Wards(models.Model):
    id = models.BigAutoField(primary_key = True)
    name = models.TextField()
    gso_id = models.TextField()
    district_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

