from django.contrib import admin
from .models import CableSparePart

class CableSparePartAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'model', 'quantity', 'remarks')
    search_fields = ('name', 'model', 'remarks')

# Register model with the admin site
admin.site.register(CableSparePart, CableSparePartAdmin)
