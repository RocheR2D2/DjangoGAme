from django.contrib import admin

# Register your models here.
from hs_game.models import Card,Card_rarity,Card_class,Card_type,Card_race,Card_set,Deck,Quantity
admin.site.register(Card_rarity)
admin.site.register(Card_class)
admin.site.register(Card_type)
admin.site.register(Card_race)
admin.site.register(Card_set)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Quantity)
