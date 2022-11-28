from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

import os
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="img/avatar.svg")
    # theme = models.CharField(max_length=10, default="dark", null=True)


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
    def getDashboardViewsURL(self):
        return reverse("dashboard:indexpage_view")
    
   
import datetime

def getFileName(request, filename):

    origiFilename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    timeNow_dir = datetime.datetime.now().strftime('%Y%m_%d')
    filename = "%s%s" % (timeNow, origiFilename)
    upload_to = 'upload/setting_assets/' + timeNow_dir + '/'
    return os.path.join(upload_to, filename)



class WebConfigirations(models.Model):
    name = models.CharField(max_length=200, default="my_site")
    logo = models.ImageField(upload_to=getFileName,
                             null=True, blank=True, default="dfdsf.png")
    discription = models.TextField(default="discription ... ")
    isdark = models.BooleanField(default=False, null=True, blank=True)
    useradmin = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)
