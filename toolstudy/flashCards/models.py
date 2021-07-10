from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=30)
    last_study = models.DateField()
    
    
class CardData(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    cards = models.ForeignKey(Deck, on_delete=models.CASCADE)

