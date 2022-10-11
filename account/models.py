from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="img/avatar.svg")


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    @property
    def imageURL(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url
   