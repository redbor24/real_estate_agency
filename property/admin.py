from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    list_display = ('town', 'town_district', 'new_building', 'address', 'floor', 'rooms_number', 'living_area',
                    'active', 'construction_year', 'price')
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_per_page = 10
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


admin.site.register(Flat, FlatAdmin)
