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
    service = models.CharField(max_length=150, null=False, default="Edit profile to update your service")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, null=True, blank=True)
    mechanic = models.OneToOneField(Mechanic, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/',default='default.jpg')
    location_address = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class WorkDone(models.Model):
    image_of_work = models.ImageField(upload_to='work/')
    user = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='works')
    added = models.DateTimeField(auto_now_add=True, null=True)
    client_name = models.CharField(max_length=100)
    client_contact = models.CharField(max_length=100)

    def get_absolute_url(self):
        return f"/work/{self.id}"

    def save_work(self):
        self.save()

    def delete_work(self):
        self.delete()

    def __str__(self):
        return f'{self.user} Work'

    @classmethod
    def get_user_works(cls,user):
        return cls.objects.filter(user=user)

    @classmethod
    def all_works(cls):
        return cls.objects.all()

    @classmethod
    def find_work(cls, work_id):
        return cls.objects.filter(id=work_id) 