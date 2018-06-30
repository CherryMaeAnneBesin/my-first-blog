from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	text = models.TextField()
	created_Date = models.DateTimeField(default= timezone.now)
	published_Date = models.DateTimeField(blank=True, null= True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

