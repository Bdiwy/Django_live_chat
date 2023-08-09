from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Message(models.Model):
    value=models.CharField(max_length=10000)    
    date=models.DateField(default=datetime.now() , blank=True)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=1000)

    
    def __str__(self):
        return self.user

