from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    inlines = [OwnerInline]
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


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phonenumber', 'owner_pure_phone']
    search_fields = ['name', 'phonenumber']
    raw_id_fields = ['flats']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['phonenumber'].label = "Номер владельца"
        form.base_fields['owner_pure_phone'].label = "Нормализованный номер владельца"
        form.base_fields['name'].label = "ФИО владельца"
        return form


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, FlatAdmin)
