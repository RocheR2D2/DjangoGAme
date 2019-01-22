from django.db import models
from django.contrib.auth.models import User
from authenticate.models import UserProfile
from django.db.models.signals import post_save

# Create your models here.

class Card_type(models.Model):
	name = models.CharField(max_length=60, unique=True)
	def __str__(self):
		return str(self.name)

class Card_class(models.Model):
	name = models.CharField(max_length=60, unique=True)
	def __str__(self):
		return str(self.name)

class Card_race(models.Model):
	name = models.CharField(max_length=60, unique=True)
	def __str__(self):
		return str(self.name)

class Card_rarity(models.Model):
	name = models.CharField(max_length=60, unique=True)
	def __str__(self):
		return str(self.name)

class Card_set(models.Model):
	name = models.CharField(max_length=60, unique=True)
	def __str__(self):
		return str(self.name)


class Card(models.Model):
	#char fields
	name = models.CharField(max_length=60, unique=True)
	card_text = models.CharField(max_length=260, null=True)
	flavor_text = models.CharField(max_length=260, null=True)
	# integer fields
	mana = models.IntegerField(default=0, null=True)
	attack = models.IntegerField(default=0, null=True)
	health = models.IntegerField(default=0, null=True)
	craftingcost = models.IntegerField(default=0, null=True)
	arcane_dust_gained = models.IntegerField(default=0, null=True)
	#image field
	card_image = models.ImageField(upload_to='cards', blank=True, null=True, unique=True)
	#foreign key
	card_rarity = models.ForeignKey(Card_rarity, on_delete=models.CASCADE, blank=True, null=True)
	card_class = models.ForeignKey(Card_class, on_delete=models.CASCADE, blank=True, null=True)
	card_type = models.ForeignKey(Card_type, on_delete=models.CASCADE, blank=True, null=True)
	card_race = models.ForeignKey(Card_race, on_delete=models.CASCADE, blank=True, null=True)
	card_set = models.ForeignKey(Card_set, on_delete=models.CASCADE, blank=True, null=True)
	user = models.ManyToManyField(UserProfile, related_name='cards', blank=True)

	def __str__(self):
		return str(self.name)


class Deck(models.Model):
	card = models.ManyToManyField(Card, related_name="decks", blank=True)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="decks")
	title = models.CharField(max_length=100, unique = True)

	def __str__(self):
		return self.title


class Quantity(models.Model):
	card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
	quantity = models.SmallIntegerField(1)

	def __str__(self):
		return str(self.quantity)


