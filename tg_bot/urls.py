from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import TutorialBotView

urlpatterns = [
    path('bot', csrf_exempt(TutorialBotView.as_view())),
]