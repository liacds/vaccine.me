from django.db import models

# Create your models here.
class MedOrganization(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    has_type_1 = models.BooleanField(default=True)
    has_type_2 = models.BooleanField(default=True)
    type_1_stock = models.BooleanField(default=True)
    type_2_stock = models.BooleanField(default=True)
    schedule_weekday = models.CharField(max_length=255, null=False)
    schedule_time = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=128, null=False)
    website = models.URLField(max_length=128, null = True)
    twogis_link = models.URLField(max_length=128, null = True)
    rayon = models.CharField(max_length=255, null=False)
    photo = models.ImageField()
    documents_needed = models.CharField(max_length=255, null=False)
    rooms = models.CharField(max_length=255, null=True)
    extra = models.CharField(max_length=255, null=True)