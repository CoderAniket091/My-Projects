from unittest.mock import DEFAULT
from urllib import request
from django.db import models

# Create your models here.
class UserFollower(models.Model):
    user = models.IntegerField()
    follower = models.CharField(max_length=100)
    followerID = models.IntegerField()

    def __str__(self):
        return self.user

class UserMain(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username