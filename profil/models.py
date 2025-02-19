from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Utilisateur(AbstractUser):
    biographie = models.CharField(max_length=100,blank=True)
    competence = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return f"{self.biographie} - {self.competence}"