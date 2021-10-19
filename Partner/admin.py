from django.contrib import admin
from .models import Partner

class PostPartner(admin.ModelAdmin):
    files = ('admin_photo')
    list_display = ['STT', 'admin_photo','partner_firstname', 'partner_lastname', 'partner_status']

    list_display_links = ['STT']

    list_filter = ['created_at', 'partner_status']

    search_fields = ['partner_firstname', 'partner_lastname']

    readonly_fields = ('partner_firstname', 'admin_photo')

# Register your models here.
admin.site.register(Partner, PostPartner)