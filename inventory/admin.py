from django.contrib import admin

# Register your models here.

from .models import PantryItem, PantryItemLine

class PantryItemInLine(admin.TabularInline):
    model = PantryItemLine
    extra = 1

class PantryItemInLineAdmin(admin.ModelAdmin):
    list_filter = ['expiry_date']

class PantryItemAdmin(admin.ModelAdmin):
    inlines = [PantryItemInLine]

admin.site.register(PantryItem, PantryItemAdmin)
admin.site.register(PantryItemLine, PantryItemInLineAdmin)
