from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_photographer = models.BooleanField(default=False)
    is_viewer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
