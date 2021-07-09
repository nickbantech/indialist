from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class List(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	website = models.CharField(max_length=100)
	contact = models.IntegerField()
	email   = models.CharField(max_length=50)
	address = models.TextField()
	pincode = models.IntegerField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User,on_delete=models.CASCADE)	

	def __str__(self):
		return self.name


	def get_absolute_url(self):

		return reverse('list-detail', kwargs={'pk': self.pk})	


      
