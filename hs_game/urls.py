from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
	path('cards/', views.listallcards, name='allcards'),
	path('my_decks/<username>', views.my_decks, name='my_decks'),
	path('first_deck/', views.first_peck, name='first_deck'),
	path('my_cards/<username>/', views.listallmycards, name='my_cards'),
	path('buy_cards/', views.buy_cards, name='buy_cards')
]

