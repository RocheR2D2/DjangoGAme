from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
# Create your models here.

class UserProfilManager(models.Manager):
	def all(self):
		query = self.get_queryset().all()
		return query


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
	following = models.ManyToManyField(User, related_name='followedby', blank=True)
	credit = models.IntegerField(default=200)
	profile = models.ImageField(upload_to='userprofiles', default="userprofiles/user.png", blank=True, null=True)
	#objects = UserProfilManager()


	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		super(UserProfile, self).save(*args, **kwargs)

		img = Image.open(self.profile.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile.path)


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

