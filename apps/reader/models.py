from django.db import models
from django.contrib.auth.models import  AbstractUser, User

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model

class Reader(AbstractUser):
    pass