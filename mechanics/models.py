from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    Username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(blank=True)

class Mechanic(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField(blank=True)