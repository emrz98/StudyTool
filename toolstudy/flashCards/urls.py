from django.urls import path
from . import views

urlpatterns = [
    path('cards/',views.ListCardData.as_view()),
]