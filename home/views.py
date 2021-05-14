from django.shortcuts import render
from rest_framework.status import *
from rest_framework.views import APIView
from .models import MedOrganization
from django.core.paginator import Paginator
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from django.conf import settings
from django.core.mail import send_mail
from smtplib import SMTPException
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity

# Create your views here.
class OrganizationView(generics.ListAPIView):
    paginate_by = 3
    model = MedOrganization
    queryset = MedOrganization.objects.all()
    serializer_class = Organization_Serializer_Short_View


class OrganizationDetailView(generics.ListAPIView):
    model = MedOrganization
    serializers = Organization_Serializer_Full_View
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        med_organization = MedOrganization.objects.filter(pk=pk).first()
        if med_organization:
            return Response(self.serializers(med_organization).data, HTTP_200_OK)
        return Response('medical organization not exist', HTTP_400_BAD_REQUEST)

class OrganizationSearchView():
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['has_type_1', 'has_type_2']
    queryset = MedOrganization.objects.all()
    model = MedOrganization
    serializer_class = Organization_Serializer_Short_View

class ContactUsView(APIView):
    def post(self, request):
        if not request.data["name"] or not request.data["email"] or not request.data["email"]:
            return Response("Param missing", HTTP_400_BAD_REQUEST)
        subject = 'Vaccine.me message'
        message = f' Message from {request.data["name"]}, at {request.data["email"]} \n {request.data["message_content"]}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['aliyawwww@gmail.com', 'vaccine.me.kz@gmail.com' ]
        try:
            send_mail(subject, message, email_from, recipient_list)
        except SMTPException as e:
            return Response(e, HTTP_400_BAD_REQUEST)
        return Response("Message successful", HTTP_200_OK)



class SearchOrganizations(APIView):
    def post(self,request):
        type = request.data['type']
        in_stock= request.data['in_stock']
        search_query = request.data['search_query']
        vector = SearchVector('name', 'address', 'rayon', 'city', 'extra', config='russian')
        query = SearchQuery(search_query, config='russian')

        if search_query:
            organizations = MedOrganization.objects.annotate(search=vector).filter(search=query)
        else:
            organizations = MedOrganization.objects.all()
        if type == "I тип":
            organizations = organizations.filter(has_type_1 = True)
            if in_stock == "в наличии":
                organizations = organizations.filter(type_1_stock=True)
        elif type == "II тип":
            organizations= organizations.filter(has_type_2 = True)
            if in_stock == "в наличии":
                organizations = organizations.filter(type_2_stock = True)

        return Response(Organization_Serializer_Short_View(organizations, many=True).data, HTTP_200_OK)



