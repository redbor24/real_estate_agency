from django.contrib import admin

from .models import Flat, Compliant, Owner


LIST_PER_PAGE = 20


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    list_display = ('town', 'town_district', 'new_building', 'address', 'floor', 'rooms_number',
                    'living_area', 'active', 'construction_year', 'price')
    fields = ['owner', 'town', 'town_district',
              'new_building', 'address', 'floor', 'rooms_number', 'living_area',
              'active', 'construction_year', 'price']
    raw_id_fields = ('like',)
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_per_page = LIST_PER_PAGE
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


class CompliantAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'compliant_text')
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    # list_display = ('user', 'phone', 'pure_phone')
    raw_id_fields = ('flat',)
    list_per_page = LIST_PER_PAGE


admin.site.register(Flat, FlatAdmin)
admin.site.register(Compliant, CompliantAdmin)
admin.site.register(Owner, OwnerAdmin)
