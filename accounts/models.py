from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30)
    birthdate = models.DateField()
    gender_choices = [
        ('M', '남성'),
        ('F', '여성'),
        ('O', '기타'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    introduction = models.TextField(blank=True)