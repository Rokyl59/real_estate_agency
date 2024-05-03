from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', 'owners_phonenumber']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owner_pure_phone'
    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'created_at']
    raw_id_fields = ['user', 'flat']


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
