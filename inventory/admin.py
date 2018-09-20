from django.contrib import admin

# Register your models here.

from .models import PantryItem, PantryItemLine

class PantryItemInLine(admin.TabularInline):
    model = PantryItemLine
    extra = 1

def upper_case_name(obj):
    return obj.name.upper()
upper_case_name.short_description = 'Name'


def capitalize_name(obj):
    return obj.name.capitalize()
upper_case_name.short_description = 'Name'



class PantryItemInLineAdmin(admin.ModelAdmin):
    list_filter = ['expiry_date', 'unit', 'pantry_item', 'pantry_item__min_quantity']
    search_fields = ['info', 'pantry_item__name', 'pantry_item__info']
    autocomplete_fields = ['pantry_item',]
    fields =  (
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


class PantryItemAdmin(admin.ModelAdmin):
    list_filter = ['category', 'unit', 'min_quantity']
    search_fields = ['info', 'name']
    inlines = [PantryItemInLine]
    # TODO: make category a model
    #autocomplete_fields = ['category',]
    fields =  (
        'name',
        'category',
        ('min_quantity', 'unit'),
        'info',
    )

    list_display = (
        capitalize_name,
        'category',
        'min_quantity',
        'unit',
        'info',
    )

admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(PantryItemLine, PantryItemInLineAdmin)
