from django.contrib import admin
from .models import Partner

class PostPartner(admin.ModelAdmin):
    list_display = ['STT', 'partner_id', 'partner_image','partner_firstname', 'partner_lastname']

    # list_display_links = ('catp_image_tag','CatPName')

    list_filter = ['created_at',]

    search_fields = ['partner_firstname', 'partner_lastname']

# Register your models here.
admin.site.register(Partner, PostPartner)