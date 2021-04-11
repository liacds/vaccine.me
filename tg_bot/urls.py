from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import TutorialBotView

urlpatterns = [
    path('recieve', csrf_exempt(TutorialBotView.as_view())),
]