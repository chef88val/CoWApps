from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

# Create your models here.
class Usuario (AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    synergy_level = models.IntegerField()
    is_team_player = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'synergy_level']


class Entrada (models.Model):
    name = models.CharField(max_length=100)
    desciption = models.CharField(max_length=600)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, blank=True, null=True )


    def __str__(self):
        return self.name
