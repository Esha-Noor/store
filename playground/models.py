from django.db import models


class CableSparePart(models.Model):
    serial_number = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100, blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='equipment_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.serial_number} - {self.name}"
