from django.db import models

# Create your models here.
class dbodd(models.Model):
    name = models.CharField(default="hell", max_length=140)