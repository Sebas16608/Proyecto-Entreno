from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)

class Profile(models.Model):
    photo = models.ImageField(upload_to='')