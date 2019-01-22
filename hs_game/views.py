from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Card, Quantity, Deck
from django.contrib.auth.models import User
from authenticate.models import UserProfile
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

def buy_cards(request):
	cardcount = Card.objects.all().count()
	cards = []
	credit = request.user.userprofile.credit
	if request.user.is_authenticated and credit >= 100:
		for i in range(6):
			random_i = randint(9, cardcount-1)
			random_c =  Card.objects.all()[random_i]
			if request.user.userprofile in random_c.user.all():
				exist = "True"
				q = Quantity.objects.filter(card=random_c, user=request.user.userprofile)
				q.quantity += 1
			
			else:
				exist = "False"
				q = Quantity.objects.create(card=random_c, user=request.user.userprofile, quantity=1)
				random_c.save()

	return render(request, 'hearthstone/buy_cards.html', {'q': q})


def my_decks(request, username):
	user = User.objects.get(username=username)
	decks = Deck.objects.all().filter(user=user.userprofile)


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


