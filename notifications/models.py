from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.


class Notifications(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=100)
