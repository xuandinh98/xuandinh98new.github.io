from django.db import models

# Create your models here.
class TickerCode(models.Model):
    category = models.CharField(max_length=5)
    product = models.CharField(max_length=5)
    service = models.CharField(max_length=5)
    unit = models.CharField(max_length=5)
    vendor = models.CharField(max_length=5)
    partner = models.CharField(max_length=5) # đối tác
    user = models.CharField(max_length=5)
    customer = models.CharField(max_length=5)
    order = models.CharField(max_length=5) # đơn hàng
    invoice = models.CharField(max_length=5) # hóa đơn
    goods_received_note = models.CharField(max_length=5) # phiếu nhập kho
    goods_delivery_note = models.CharField(max_length=5) # phiếu xuất kho
    inventory_sheet = models.CharField(max_length=5) # kiểm kê
    shipping_unit = models.CharField(max_length=5) # đơn vị vận chuyển

class Unit(models.Model):
    STT = models.BigAutoField(primary_key = True)
    unit_id = models.CharField(max_length=10)
    unit_name = models.TextField()
    unit_slug = models.CharField(max_length=255)
    unit_status = models.IntegerField(default=1)
    created_at = models.DateField()
    updated_at = models.DateField()

class CategoryProduct(models.Model):
    STT = models.BigAutoField(primary_key = True)
    category_id = models.CharField(max_length=10)
    category_name = models.TextField()
    category_parent_id = models.IntegerField()
    category_slug = models.CharField(max_length=255)
    category_status = models.IntegerField(default=1)
    created_at = models.DateField()
    updated_at = models.DateField()

