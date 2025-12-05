from django.db import models


class BlockCStationaryItem(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, verbose_name='Unit of Measure', blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.PositiveIntegerField(default=0)
    open = models.PositiveIntegerField(default=0)
    in_stock = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='stationary_images/', blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    # new fields
    person = models.CharField(max_length=100, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sr_no} - {self.item_name}"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block C (Stationary Items)"


class BlockAConsumableItem(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, verbose_name='Unit of Measure', blank=True, null=True)
    amount_per_box_pack_roll = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    full_boxes_packs_rolls = models.PositiveIntegerField(default=0)
    open = models.PositiveIntegerField(default=0)
    in_stock = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='consumable_images/', blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    # new fields
    person = models.CharField(max_length=100, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sr_no} - {self.item_name}"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block A (Consumable Items)"







#from django.db import models
from django.utils.html import mark_safe

class MiscItem(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.CharField(max_length=50, blank=True, null=True)
    open = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='misc_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Misc items"



class FixedAssets(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.CharField(max_length=50, blank=True, null=True)
    open = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='assets_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block B (Fixed Assets)"





class PPEs(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.CharField(max_length=50, blank=True, null=True)
    open = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='ppes_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block C (PPE's)"






class SpareItems(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.CharField(max_length=50, blank=True, null=True)
    open = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='ppes_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block D (Spare Items)"





class Keys(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    quantity_mentioned = models.CharField(max_length=50, blank=True, null=True)
    actual_quantity = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='ppes_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Block E (Keys)"





class TeaItems(models.Model):
    sr_no = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    amount_per_box_pack_roll = models.CharField(max_length=50, blank=True, null=True)
    full_boxes_packs_rolls = models.CharField(max_length=50, blank=True, null=True)
    open = models.CharField(max_length=50, blank=True, null=True)
    old_stock = models.CharField(max_length=50, blank=True, null=True)
    in_stock = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    person = models.CharField(max_length=255, blank=True, null=True)
    dispatch_loc = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='ppes_images/', blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.sr_no})"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')
        return "No image"
    image_tag.short_description = "Image"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Tea Items"






#thirdrail model


from django.db import models
from django.utils.safestring import mark_safe

class ThirdRail(models.Model):
    # Required field
    sr_no = models.IntegerField()


    # All other fields optional
    product_id = models.CharField(max_length=100, blank=True, null=True)
    register_page_no = models.CharField(max_length=100, blank=True, null=True)

    tools_and_spares = models.CharField(max_length=255, blank=True, null=True)   # NEW COLUMN
    cabinet_no = models.CharField(max_length=100, blank=True, null=True)
    rack_no = models.CharField(max_length=100, blank=True, null=True)

    product_description = models.TextField(blank=True, null=True)
    product_category = models.CharField(max_length=255, blank=True, null=True)

    store_stock = models.CharField(max_length=50, blank=True, null=True)

    column4 = models.CharField(max_length=255, blank=True, null=True)
    column3 = models.CharField(max_length=255, blank=True, null=True)
    column2 = models.CharField(max_length=255, blank=True, null=True)
    column1 = models.CharField(max_length=255, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)

    # image = models.ImageField(upload_to='tea_items_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id or 'Item'} ({self.sr_no})"

    class Meta:
        ordering = ['sr_no']
        verbose_name_plural = "Store Inspection Checklist (ThirdRail)"
