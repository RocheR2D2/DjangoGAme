from django.db import models
from authenticate.models import UserProfile
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
	title = models.CharField(max_length=60)
	content = models.CharField(max_length=200)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.title)