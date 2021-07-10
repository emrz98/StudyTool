from rest_framework.serializers import ModelSerializer
from rest_framework.utils import field_mapping
from .models import CardData, Deck
class CardDataSerializer(ModelSerializer):
    class Meta:
        model = CardData
        fields = ['question', 'answer']

class DeckSerializer(ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

