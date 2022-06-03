from django.db import models

# Create your models here.
class FollowData(models.Model):
    username1 = models.CharField(max_length=100)
    username2 = models.CharField(max_length=100)
    def __str__(self):
        return self.username1

class UserMain(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username