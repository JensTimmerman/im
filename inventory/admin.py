from django.contrib import admin

# Register your models here.

from .models import PantryItem, PantryItemLine

class PantryItemInLine(admin.TabularInline):
    model = PantryItemLine
    extra = 1

class PantryItemInLineAdmin(admin.ModelAdmin):
    list_filter = ['expiry_date']
    list_display = (
        'pantry_item',
        'quantity',
        'expiry_date',
        'size',
        'unit',
        'info',
    )


class PantryItemAdmin(admin.ModelAdmin):
    inlines = [PantryItemInLine]
    list_display = (
        'name',
        'category',
        'min_quantity',
        'unit',
        'info',
    )

admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(PantryItemLine, PantryItemInLineAdmin)
