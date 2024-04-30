from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Products(AbstractUser):
    p_name = models.CharField(max_length=30, default='')
    p_text = models.TextField(blank=True)
    p_images = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    introduction = models.TextField(blank=True)