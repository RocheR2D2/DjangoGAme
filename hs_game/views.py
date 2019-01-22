from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Card, Quantity, Deck
from django.contrib.auth.models import User
from random import randint


# Create your views here.
def listallcards(request):
   	queryset = Card.objects.all()
   	paginator = Paginator(queryset, 10)
   	page = request.GET.get('page')
   	cards = paginator.get_page(page)
    
   	return render(request, 'hearthstone/allcards.html', {'cards': cards})

def listallmycards(request,username):

	user = User.objects.get(username=username)
	quantity = Quantity.objects.all().filter(user=user.userprofile)
	queryset = Card.objects.all().filter(user=user.userprofile)
	paginator = Paginator(queryset, 10)
	page = request.GET.get('page')
	cards = paginator.get_page(page)

	return render(request, 'hearthstone/my_cards.html', {'cards': cards, 'quantity': quantity})


def my_decks(request):
	decks = Deck.objects.all().filter(user=request.user.userprofile)

	return render(request, 'hearthstone/my_decks.html', {'decks': decks})

def create_deck(request):
	user = request.user.userprofile

	return render(request, 'hearthstone/new_deck.html', {})


def first_peck(request):

	user = request.user
	quantity = Quantity.objects.all().filter(user=user.userprofile)


	if user.is_authenticated:
		if quantity.count() == 0:
			deck = Deck.objects.create(user=user.userprofile, title=user.username)
			for i in range(10):
				newcard = Card.objects.all()[i]
				newcard.user.add(user.userprofile)
				newQuantity = Quantity.objects.create(card=newcard, user=user.userprofile, quantity=1)
				deck.card.add(newcard)




			return render(request, 'hearthstone/new_deck.html', {'deck': deck.card.all()})

		return render(request, 'hearthstone/new_deck.html', {'new': 'old'})


