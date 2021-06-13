from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	usertype=models.CharField(max_length=30)
	mobile=models.CharField(max_length=30)
	address=models.CharField(max_length=300)