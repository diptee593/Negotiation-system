from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    # phone = models.IntegerField()

    def __str__(self):
        return self.username
    

