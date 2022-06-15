from django.db import models
import uuid
# Create your models here.


class Topic(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Title: {self.title} - Text: {self.text} - Created: {self.created}{self.created_by} - ID: {self.id}'
