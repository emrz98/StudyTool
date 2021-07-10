from django.http.response import Http404
from django.shortcuts import render
import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CardDataSerializer, DeckSerializer
from .models import CardData, Deck

class ListCardData(APIView):
    def get(self, request):
        card_data = CardData.objects.all()
        card_serializer = CardDataSerializer(card_data, many=True)
        return Response(card_serializer.data)

    def post(self, request):
        serializer = CardDataSerializer(request.data)
        if serializer.is_valid():
            serializer.save() 

class ListCardDetail(APIView):
    def get_card(self, pk):
        try:
            card = CardData.objects.get(id=pk)
            return card
        except:
            raise Http404
    def put(self, request, pk):
        card = self.get_card(pk)
        serializer = CardDataSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_card(pk)
        card.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class ListDeck(APIView):
    def get(self, request):
        card_data = Deck.objects.all()
        serializer = DeckSerializer(card_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardDataSerializer(request.data)
        if serializer.is_valid():
            serializer.save() 