from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class paperRecord(models.Model):
	name   		 = models.CharField(max_length=40)
	email        = models.CharField(max_length=40)
	mobileNumber = models.CharField(max_length=10)
	title 		 = models.CharField(max_length=50)
	body 	 	 = models.TextField()
	file 		 = models.FileField(default='none.pdf')
	timestamp	 = models.DateTimeField(auto_now_add=True)
	author		 = models.ForeignKey(User,on_delete=models.PROTECT,default=None)

	def __str__(self):
		date = str(self.timestamp.day)+"/"+str(self.timestamp.month)
		return self.name+"   "+date