from django.contrib import admin
from .models import Partner

class PostPartner(admin.ModelAdmin):
    files = ('admin_photo')
    list_display = ['STT', 'partner_id', 'admin_photo','partner_firstname', 'partner_lastname']

    list_display_links = ['partner_id']

    list_filter = ['created_at',]

    search_fields = ['partner_firstname', 'partner_lastname']

    readonly_fields = ('partner_firstname', 'admin_photo')

# Register your models here.
admin.site.register(Partner, PostPartner)