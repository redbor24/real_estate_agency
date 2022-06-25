from django.contrib import admin

from .models import Flat, Compliant, Owner

LIST_PER_PAGE = 20


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat',)
    verbose_name = 'Квартира'
    verbose_name_plural = 'Квартиры'
    extra = 0


class CompliantsInline(admin.TabularInline):
    model = Compliant
    raw_id_fields = ('user', 'flat')
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'
    extra = 0


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)
    verbose_name = 'Владелец'
    verbose_name_plural = 'Владельцы'
    extra = 0


class LikesInline(admin.TabularInline):
    model = Flat.likes.through
    raw_id_fields = ('user',)
    verbose_name = 'Кто лайкнул'
    verbose_name_plural = 'Кто лайкнул'
    extra = 0


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    list_display = ('town', 'town_district', 'new_building', 'address', 'floor', 'rooms_number',
                    'living_area', 'active', 'construction_year', 'price')
    fields = ['town', 'town_district',
              'new_building', 'address', 'floor', 'rooms_number', 'living_area',
              'active', 'construction_year', 'price']
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_per_page = LIST_PER_PAGE
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    inlines = [OwnersInline, CompliantsInline, LikesInline]
    exclude = ('owner',)


@admin.register(Compliant)
class CompliantAdmin(admin.ModelAdmin):
    list_display = ('flat', 'user', 'text', )
    raw_id_fields = ('user', 'flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'phone', 'pure_phone', )
    list_per_page = LIST_PER_PAGE
    exclude = ('flat', 'flats',)
    inlines = [FlatsInline]
