from django.contrib import admin
from django.utils.html import format_html
from .models import BlockCStationaryItem, BlockAConsumableItem
from .models import MiscItem
from .models import FixedAssets
from .models import PPEs
from .models import SpareItems
from .models import Keys
from .models import TeaItems


from django.urls import reverse
from django.utils.html import format_html

# Optional: custom admin index
admin.site.index_title = "E&M Inventory Management Admin"
admin.site.site_header = "E&M Power Supply & Third Rail"
admin.site.site_title = "Inventory Admin"

# Add a "Download Excel" button on the main admin page
def export_dashboard_link():
    url = reverse('export_dashboard')
    return format_html('<a class="button" href="{}" target="_blank">Export Inventory</a>', url)

admin.site.index_template = 'admin/index.html'

from django.http import HttpResponseRedirect

# @admin.register(YourModel)
# class YourModelAdmin(admin.ModelAdmin):

#     actions = ["go_to_export"]

#     def go_to_export(self, request, queryset):
#         return HttpResponseRedirect("/playground/exports/")

#     go_to_export.short_description = "Go to Export Page"


# 🧾 Admin for Block C (Stationary)
@admin.register(BlockCStationaryItem)
class BlockCStationaryItemAdmin(admin.ModelAdmin):
    list_display = (
        'sr_no',
        'item_name',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',  # show image thumbnail
        'remarks',
        'created_at',
        'updated_at',
    )
    search_fields = ('item_name', 'location', 'person', 'dispatch_loc')
    list_filter = ('location', 'person', 'dispatch_loc')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')



    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"

    


# 🧾 Admin for Block A (Consumables)
@admin.register(BlockAConsumableItem)
class BlockAConsumableItemAdmin(admin.ModelAdmin):
    list_display = (
        'sr_no',
        'item_name',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )
    search_fields = ('item_name', 'location', 'person', 'dispatch_loc')
    list_filter = ('location', 'person', 'dispatch_loc')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"








@admin.register(MiscItem)
class MiscItemAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50




@admin.register(FixedAssets)
class FixedAssetsAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50





@admin.register(PPEs)
class PPEsAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50




@admin.register(SpareItems)
class SpareItemsAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50





@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'quantity_mentioned',
        'actual_quantity',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50





@admin.register(TeaItems)
class TeaItemsAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'item_name',
        'item_description',
        'uom',
        'amount_per_box_pack_roll',
        'full_boxes_packs_rolls',
        'open',
        'old_stock',
        'in_stock',
        'location',
        'person',
        'dispatch_loc',
        'image_tag',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('item_name', 'location')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('uom', 'location')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')


    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', obj.image.url)
        return "—"
    image_tag.short_description = "Image"


    # Optional: number of items per page
    list_per_page = 50



#thirdrail

from django.contrib import admin
from django.utils.html import format_html
from .models import ThirdRail

@admin.register(ThirdRail)
class ThirdRailAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = (
        'sr_no',
        'product_id',
        'register_page_no',
        'tools_and_spares',
        'cabinet_no',
        'rack_no',
        'product_description',
        'product_category',
        'store_stock',
        'column4',
        'column3',
        'column2',
        'column1',
        'remarks',
        'created_at',
        'updated_at',
    )

    # Fields you can search by
    search_fields = ('tools_and_spares', 'cabinet_no', 'rack_no')

    # Fields you can filter by (right-hand sidebar)
    list_filter = ('product_category', 'cabinet_no', 'rack_no')
    ordering = ('sr_no',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('sr_no')

    # Optional image field if your model has an image (remove if not needed)
    def image_tag(self, obj):
        if hasattr(obj, 'image') and obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:6px;object-fit:cover;"/>', 
                obj.image.url
            )
        return "—"
    image_tag.short_description = "Image"

    # Optional: number of items per page
    list_per_page = 50





###########################################################

from django.contrib import admin

class GlobalAdmin(admin.AdminSite):
    class Media:
        css = {
            'all': ('playground/admin_scroll.css',)
        }

admin.site.__class__ = GlobalAdmin


############################################################


