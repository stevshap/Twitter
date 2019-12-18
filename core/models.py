from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    users = models.ManyToManyField(User, related_name='users')
    likes = models.FloatField()
    date = models.DateField()