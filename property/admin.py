from django.contrib import admin

from .models import Flat, Compliant, Owner

LIST_PER_PAGE = 20


class FlatsInline(admin.TabularInline):
    model = Owner.flat.through
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
    model = Owner.flat.through
    raw_id_fields = ('owner',)
    verbose_name = 'Владелец'
    verbose_name_plural = 'Владельцы'
    extra = 0


class LikesInline(admin.TabularInline):
    model = Flat.like.through
    raw_id_fields = ('user',)
    verbose_name = 'Кто лайкнул'
    verbose_name_plural = 'Кто лайкнул'
    extra = 0


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    list_display = ('town', 'town_district', 'new_building', 'address', 'floor', 'rooms_number',
                    'living_area', 'active', 'construction_year', 'price')
    fields = ['town', 'town_district',
              'new_building', 'address', 'floor', 'rooms_number', 'living_area',
              'active', 'construction_year', 'price']
    raw_id_fields = ('like',)
    readonly_fields = ['created_at']
    list_editable = ['new_building']
    list_per_page = LIST_PER_PAGE
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    inlines = [OwnersInline, CompliantsInline, LikesInline]
    exclude = ('owner',)


class CompliantAdmin(admin.ModelAdmin):
    list_display = ('compliant_text', )
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_per_page = LIST_PER_PAGE
    exclude = ('flat', )
    inlines = [FlatsInline]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Compliant, CompliantAdmin)
admin.site.register(Owner, OwnerAdmin)
