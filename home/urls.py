from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('medorganizations', OrganizationView.as_view(), name='all_clinic'),
    path('medorganizations/<int:pk>', OrganizationDetailView.as_view(), name='clinic'),
    path('contact_us', ContactUsView.as_view(), name='email'),
    path('medorganizations/search', SearchOrganizations.as_view())

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)