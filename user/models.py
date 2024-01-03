from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	phone=models.CharField(max_length=15)
	photo=models.ImageField(upload_to='user_photo/', default='1.jpg')

	def __str__(self):
		return self.username