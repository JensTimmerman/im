from django.contrib import admin

from .models import PantryItem, PantryItemLine, Unit, Category, Location


class PantryItemInLine(admin.TabularInline):
    model = PantryItemLine
    extra = 1



class LocationInLine(admin.TabularInline):
    model = Location
    extra = 1

def upper_case_name(obj):
    return obj.name.upper()
upper_case_name.short_description = 'Name'


def capitalize_name(obj):
    return obj.name.capitalize()
upper_case_name.short_description = 'Name'


class PantryItemLineAdmin(admin.ModelAdmin):
    list_filter = ['expiry_date', 'pantry_item__unit', 'pantry_item', 'pantry_item__min_quantity']
    search_fields = ['info', 'pantry_item__name', 'pantry_item__info']
    autocomplete_fields = ['pantry_item']

    readonly_fields = ['unit']
    fields = (
        'pantry_item',
        'quantity',
        'expiry_date',
        ('size', 'unit'),
        'info',
    )

    list_display = (
        'pantry_item',
        'quantity',
        'expiry_date',
        'size',
        'unit',
        'info',
    )


class AutocompleteAdmin(admin.ModelAdmin):
    """Class used to satisfy an admin check"""
    search_fields = ["name"]


class LocationAdmin(AutocompleteAdmin):
    inlines = [LocationInLine]


class PantryItemAdmin(admin.ModelAdmin):
    list_filter = ['category', 'unit', 'min_quantity', 'location']
    search_fields = ['info', 'name', 'category__name', 'unit__name']
    autocomplete_fields = ['category', 'unit']
    inlines = [PantryItemInLine]

    # TODO: make category a model
    #autocomplete_fields = ['category',]
    fields = (
        'name',
        'category',
        ('min_quantity', 'unit'),
        'location',
        'info',
        'expiry_duration',
    )

    list_display = (
        capitalize_name,
        'category',
        'min_quantity',
        'unit',
        'info',
    )

admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(PantryItemLine, PantryItemLineAdmin)
admin.site.register(Unit, AutocompleteAdmin)
admin.site.register(Category, AutocompleteAdmin)
admin.site.register(Location, LocationAdmin)
