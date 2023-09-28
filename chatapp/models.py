from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUsers(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    
    def __str__(self):
        return self.username