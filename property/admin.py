from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    list_display = ('town', 'town_district', 'address', 'floor', 'rooms_number', 'living_area', 'active',
                    'construction_year', 'price')


admin.site.register(Flat, FlatAdmin)
