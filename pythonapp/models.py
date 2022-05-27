from django.db import models
import uuid

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    born = models.DateField()

class Topic(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    topic=models.CharField(max_length=30)
    text=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)

class Users(models.Model):
    nickname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=30)
    message=models.CharField(max_length=500)