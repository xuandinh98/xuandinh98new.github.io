from django.contrib import admin
from django.contrib.auth.models import Group
from .models import TickerCode
from .models import Unit
from .models import CategoryProduct

# Register your models here.
admin.site.site_header = "Dashboard"

admin.site.register(TickerCode)
admin.site.register(Unit)
admin.site.register(CategoryProduct)
admin.site.unregister(Group)