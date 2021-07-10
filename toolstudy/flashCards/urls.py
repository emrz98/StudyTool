from django.urls import path
from . import views

urlpatterns = [
    path('cards/',views.ListCardData.as_view()),
    path('cards/<int:pk>', views.ListCardDetail.as_view()),
    path('decks/', views.ListDeck.as_view())
]