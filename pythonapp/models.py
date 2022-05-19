from unicodedata import name
from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    born = models.DateField()
