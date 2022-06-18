from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_time = models.DateTimeField()
    Published_date = models.DateTimeField()
