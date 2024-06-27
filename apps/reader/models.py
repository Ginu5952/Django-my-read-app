from django.db import models
from django.contrib.auth.models import  AbstractUser, User

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model

class Reader(AbstractUser):
    # if no explicit primary key is defined, django will generate an id for us.
    # Class attribute will represent fields in our table
    # By default django fields are not null

    username = models.CharField(max_length=50, primary_key=True)
    # null = True set the null field when used on the terminal
    # blank= True set the null field when used on the dashboard
    title = models.CharField(max_length=5, null=True, blank=True)
    # if you want to remove te default, just set it to None
    # email = None
    