from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    problems_solved = models.IntegerField(default=0)
   
    def __str__(self):
        return self.email


class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Solution(models.Model):
    user_email = models.EmailField(default=True)
    code = models.TextField()

    def __str__(self):
        return self.user_email
