from django.db import models
from home.models import MedOrganization

# Create your models here.
class ChatContext(models.Model):
    user = models.CharField(max_length=255, null=False)
    organization = models.ForeignKey(MedOrganization, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=255, null=True)
    update = models.CharField(max_length=255, null=True)