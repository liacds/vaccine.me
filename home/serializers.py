from rest_framework import serializers
from .models import MedOrganization


class Organization_Serializer_Short_View(serializers.ModelSerializer):
    class Meta:
        model = MedOrganization
        fields = ['pk', 'name', 'address','has_type_1', 'has_type_2', 'phone_number', 'schedule_weekday', 'schedule_time', 'twogis_link', 'website']

class Organization_Serializer_Full_View(serializers.ModelSerializer):
    class Meta:
        model = MedOrganization
        fields = '__all__'